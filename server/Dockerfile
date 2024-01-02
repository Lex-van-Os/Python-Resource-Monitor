# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make your script executable
RUN chmod +x ./usage.sh

# Run your script when the container launches
CMD ["./usage.sh"]