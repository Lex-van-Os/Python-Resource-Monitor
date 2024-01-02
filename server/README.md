# Server Application for Python-Resource-Monitor

This is the server application for the Python-Resource-Monitor project. The server listens for results given by the client side, to then provide further insights into resource usage.

## Prerequisites

- Docker installed on your machine. You can download Docker [here](https://www.docker.com/products/docker-desktop).

## Installation

1. Clone the Python-Resource-Monitor repository to your local machine.

```sh
git clone https://github.com/yourusername/Python-Resource-Monitor.git
```

## Running the Docker Container

1. Build the Docker image from the Dockerfile:

```sh
docker build -t python-resource-monitor-server .
```

2. Run the Docker container: 

```sh
docker run -d --name prmc python-resource-monitor-server
```