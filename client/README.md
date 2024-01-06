# Client Application for Python-Resource-Monitor

This is the client application for the Python-Resource-Monitor project. It monitors local resource usage and sends the data to a server.

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
docker build -t monitor-client:1.0.0 .
```

2. Run the Docker container: 

```sh
docker run -d --name monitor-client monitor-client:1.0.0
```

3. Re-run the Docker container:

```sh
docker start monitor-client
```