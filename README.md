<p align="center">
  <a href="https://scalekit.com" target="_blank" rel="noopener noreferrer">
    <picture>
      <img src="https://cdn.scalekit.cloud/v1/scalekit-logo-dark.svg" height="64">
    </picture>
  </a>
  <br/>
</p>
<h1 align="center">
  Scalekit FastAPI Example App
</h1>

<h4 align="center">
Scalekit helps you ship Enterprise Auth in days.

This FastAPI Sample App showcases the Scalekit Official Python SDK implementation.
</h4>

## Getting Started

1. [Sign up](https://scalekit.com) for a Scalekit account.
2. Get your ```env_url```, ```client_id``` and ```client_secret``` from the Scalekit dashboard.

## How to Run
```sh
# Add ReactJS submodule for frontend elements 
git clone --recursive https://github.com/scalekit-developers/shared-ui-for-examples.git
```

```sh
# Install scalekit-fastapi-example dependencies from requirements file using below cmd 
pip install -r requirements
```

```sh
# Run following command to create .env file
add cp .env.example .env
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
