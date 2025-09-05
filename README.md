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

[![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<h4 align="center">
Scalekit is the <strong>auth stack for AI apps</strong> - from human authentication to agent authorization.

This FastAPI example demonstrates how to implement both traditional B2B authentication (SSO, passwordless) and cutting-edge agentic workflows using Scalekit's Python SDK.
</h4>

## 🤖 What This Demo Shows

- **Agent-First Authentication**: MCP integration with delegated consent
- **Human SSO Integration**: Enterprise SAML/OIDC authentication flows
- **Token Vault**: Secure per-user, per-tool token management
- **Passwordless Auth**: Modern authentication without passwords
- **Fast API Performance**: High-performance async Python framework
- **Session Management**: Secure user state handling

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
