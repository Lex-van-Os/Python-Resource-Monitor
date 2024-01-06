# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make your script executable
RUN chmod +x /app/monitor.sh

# List the contents of the /app directory
RUN ls -la /app

# Log the current path
RUN echo "Current path: $PWD"

# Update package lists and upgrade new installations
RUN apt-get update

# Install necessary package(s) for script
RUN apt-get install -y sysstat

# Run your script when the container launches
CMD ["/app/monitor.sh"]
