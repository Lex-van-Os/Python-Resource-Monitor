# Stage 1: Build Python application
FROM python:3.12-slim AS python-builder

# Copy Python application code
COPY app /app

# Stage 2: Build final image with Python application and NGINX
FROM ubuntu:23.10

# Update package lists
RUN apt-get update

# Install Python, pip, Nginx, and InfluxDB client
RUN apt-get install -y python3 python3-pip nginx

RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install influxdb-client[async] Flask --break-system-packages

# Clean up package lists to reduce image size
RUN rm -rf /var/lib/apt/lists/*

# Copy Python application code from the 1st stage
COPY --from=python-builder /app /app

# Copy NGINX configuration files
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Set the working directory
WORKDIR /app

# Expose port 80 for the NGINX server
EXPOSE 8080

# Command to start both Python server and NGINX
CMD ["bash", "-c", "python3 server.py & nginx -g 'daemon off;'"]