import os
from typing import Optional, Annotated

import uvicorn
from dotenv import load_dotenv
from faker import Faker
from fastapi import FastAPI, Cookie
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from options.scalekit import AuthorizationUrlOptions, CodeAuthenticationOptions
from pydantic import BaseModel
from scalekit_client import Scalekit
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse

load_dotenv()

app = FastAPI()

url = os.environ['SCALEKIT_ENV_URL']
client_id = os.environ['SCALEKIT_CLIENT_ID']
client_secret = os.environ['SCALEKIT_CLIENT_SECRET']
redirect_uri = os.environ['AUTH_REDIRECT_URI']
host = os.environ['HOST']

scale = Scalekit(url, client_id, client_secret)
users = {}


class WebFiles(StaticFiles):
    async def get_response(self, path: str, scope):
        try:
            response = await super().get_response(path, scope)
            return response
        except HTTPException as exp:
            if exp.status_code == 404:
                response = await super().get_response('.', scope)
                return response
            raise exp


class Login(BaseModel):
    connectionId: Optional[str] = None
    organizationId: Optional[str] = None
    email: Optional[str] = None


@app.get("/auth/me")
def auth_me(uid: Annotated[str | None, Cookie()] = None):
    if not uid:
        return JSONResponse(status_code=401, content={"message": "User data not found"})
    user = users[uid]
    if not user:
        return JSONResponse(status_code=401, content={"message": "User not found"})
    return user


@app.post("/auth/login")
async def auth_login(login: Login):
    options = AuthorizationUrlOptions()
    options.connection_id = login.connectionId
    options.organization_id = login.organizationId
    options.login_hint = login.email
    options.state = ''.join(Faker().text().replace(' ', '').strip()[:15]).lower()

    auth_url = scale.get_authorization_url(redirect_uri=redirect_uri, options=options)
    return {'url': auth_url}


@app.get("/auth/callback")
async def auth_callback(code: str | None = None, error_description: str | None = None):
    if error_description:
        return JSONResponse(status_code=400, content=error_description)
    options = CodeAuthenticationOptions()
    options.code = code
    options.redirect_uri = redirect_uri
    result = scale.authenticate_with_code(options=options)
    user = result['user']
    uid = user['id']
    users[uid] = user
    response = RedirectResponse(url='/profile', status_code=303)
    response.set_cookie(key='uid', value=uid, httponly=False)
    return response


@app.post("/auth/logout")
async def auth_logout():
    response = JSONResponse(status_code=200, content='')
    response.delete_cookie(key='uid', httponly=False)
    return response


app.mount("/", WebFiles(directory="web/build", html=True), name="web/build")


if __name__ == "__main__":
    uvicorn.run(app, host=host, port=8080)
