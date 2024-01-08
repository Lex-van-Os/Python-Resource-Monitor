@echo off

REM Navigate to the client directory
cd ..\server

REM Build the Docker image
docker build -t monitor-server:1.0.0 .

REM Stop and remove the old container if it exists
docker rm -f monitor-server

REM Run the new Docker container
docker run -d --name monitor-server -p 80:80 monitor-server:1.0.0

REM Navigate back to the commands directory
cd ..\commands
