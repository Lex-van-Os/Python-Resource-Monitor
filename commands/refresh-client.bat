@echo off

REM Navigate to the client directory
cd ..\client

REM Build the Docker image
docker build --progress=plain --no-cache -t monitor-client:1.0.0 .

REM Stop and remove the old container if it exists
docker rm -f monitor-client

REM Run the new Docker container
docker run -d --name monitor-client monitor-client:1.0.0

REM Navigate back to the commands directory
cd ..\commands
