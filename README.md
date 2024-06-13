<p align="left">
  <a href="https://scalekit.com" target="_blank" rel="noopener noreferrer">
    <picture>
      <img src="https://cdn.scalekit.cloud/v1/scalekit-logo-dark.svg" height="64">
    </picture>
  </a>
  <br/>
</p>
<h1 align="left">
  FastAPI Example App
</h1>

<a href="https://scalekit.com" target="_blank" rel="noopener noreferrer">Scalekit</a> is an Enterprise Authentication Platform purpose built for B2B applications. This Go SDK helps implement Enterprise Capabilities like Single Sign-on via SAML or OIDC in your Golang applications within a few hours.

<div>
📚 <a target="_blank" href="https://docs.scalekit.com">Documentation</a> - 🚀 <a target="_blank" href="https://docs.scalekit.com">Quick-start Guide</a> - 💻 <a target="_blank" href="https://docs.scalekit.com/apis">API Reference</a>
</div>
<hr />

## Pre-requisites

1. [Sign up](https://scalekit.com) for a Scalekit account.
2. Get your ```env_url```, ```client_id``` and ```client_secret``` from the Scalekit dashboard.

## How to Run
```sh
# Add ReactJS submodule for frontend elements 
git clone --recursive https://github.com/scalekit-inc/scalekit-fastapi-example.git
```

```sh
# Install scalekit-fastapi-example dependencies from requirements file using below cmd 
pip install -r requirements
```

```sh
# Run following command to create .env file
cp .env.example .env
```

```sh
# Update .env file with env_url, client_id and client_secret fetched from the Scalekit dashboard as below
SCALEKIT_ENV_URL = env_url
SCALEKIT_CLIENT_ID = client_id
SCALEKIT_CLIENT_SECRET = client_secret
```

```sh
# Run the development server:
python3 main.py
```

```sh
Open http://localhost:8080 with your preferred browser
```

## API Reference
See the [Scalekit API docs](https://docs.scalekit.com) for more information about the API and authentication.
