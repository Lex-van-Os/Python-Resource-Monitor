# Server Application for Python-Resource-Monitor

This is the server application for the Python-Resource-Monitor project. The server listens for results given by the client side, to then provide further insights into resource usage.

## Prerequisites

- Docker installed on your machine. You can download Docker [here](https://www.docker.com/products/docker-desktop).

## Installation

Installation and configuration of the Server can be done by executing the corresponding automation file in the `commands` folder.

### Windows

1. refresh-client: Automatically sets up the Docker environment

### Unix

1. WIP

## Functionality

The Server application is set-up using the `asyncio` Python library. With this, an asynchronous socket functionality is realized, which can handle incoming client application statistics.

### Used packages

1. asyncio
2. Flask (WIP)
3. logging
