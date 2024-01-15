# Python-Resource-Monitor

## Description

A resource monitoring system written in Python. The client monitors local resource usage, sending the resource usage data to the server. The server stores this data in a database, logs it, and displays it through a UI. Processes are automated using bash and Docker. This program simulates multiple standalone clients sending log data to the server, which then collects and visualizes the data.

## Functionality

### Client application

- A **client-server** application where the **client** sends resource usage data (CPU usage, memory, disk usage, etc.) to the **server**.
  - Resource monitoring using bash scripts and tools like top, ps, etc.
  - Periodically collects resource usage data (e.g., every 5 seconds).
- Periodically sends resource usage data over the **network** to the **server**.

---

Functionality: `Python`, `psutil` OR `Bash` (top, ps, etc.), `asyncio`

### Network

- Connection between **client** (local PC) and **server** (Docker).
- **Client**(s) can communicate with the **server** through communication with the container.
- TCP/IP with asyncio.

---

Functionality: `TCP`

### Server application

- Runs on Docker.
- **Server** receives resource data from multiple **clients**.
- **Server** stores received data in InfluxDB database for further processing.
- Contains a web-based interface to display visualized data through InfluxDB.

---

Functionality: `InfluxDB`

### Visualization

- Visualization using charts/graphs based on InfluxDB data.
  - Makes use of InfluxDB interface
- Accessible through standalone database container endpoint

---

Functionality: `InfluxDB`

### Automation

- Bash scripts for:
  - Deployment of **client** and **server** applications.
  - Configuration of **client** and **server** applications.
  - Starting and stopping monitors.
  - Logging.

---

Functionality: `Bash`, `Docker`, `Markdown`

### Logging

- Logging of relevant information in the terminal using tools like grep and awk.

---

Functionality: `Built-in logging`, `logging`

## Starting the application

1. Navigate to the correct directory
   Ensure that you're inside of the project root folder

2. Run the following command:

```sh
docker-compose up
```

3. Reset & recreate the application entirely:

```sh
docker-compose up --build --force-recreate
```

## Debugging the application

- Check Docker container information:

```sh
docker ps
```

- Check Docker containers network information:

```sh
docker network inspect python-resource-monitor_monitor-network
```

## Application flow

### Client(s)

Multiple client applications generate log data as part of their operation. These logs are important for understanding the behavior of the application, diagnosing problems, and analyzing performance.

The client applications send their log data to a central server over TCP. TCP (Transmission Control Protocol) is a reliable, ordered, and error-checked delivery of a stream of bytes from one application to another on a network. This ensures that all log data is received correctly and in order.

### Server

The server receives the log data from multiple clients asynchronously. This means that the server can handle multiple connections at the same time, without waiting for one client to finish sending log data before starting to receive log data from another client.

The server's job is to collect the log data from all the clients and prepare it for storage. This might involve parsing the log data, filtering it, or aggregating it in some way.

### Database

Once the server has collected and processed the log data, it stores the data in a database. The database provides a way to persistently store the log data, so it can be queried and analyzed later.

Data can then be viewed through the User Interface provided by InfluxDB. After having logged in, the user can analyse the metrics of the individual client applications by making use of the provided dashboards.

This setup allows for centralized log collection and storage, making it easier to monitor and analyze the behavior of all the client applications from a single location.

### Grafana

To provide extra functionality for visualization, an integration with Grafana is supplied together with this application. Having configured the InfluxDB database environment, one can configure a corresponding Grafana environment by making use of the InfluxDB credentials.

By making use of Grafana, you can create a real time monitoring dashboard, comparable to the dashboard offered by InfluxDB. The Grafana dashboard can be completely personalized to the user's needs.
