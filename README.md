# Python-Resource-Monitor

## Description

A resource monitoring system written in Python. The client monitors local resource usage, sending the resource usage data to the server. The server stores this data in a database, logs it, and displays it through a UI. Processes are automated using bash and Docker.

## Functionality

### Client application

- A **client-server** application where the **client** sends resource usage data (CPU usage, memory, disk usage, etc.) to the **server**.
  - Resource monitoring using bash scripts and tools like top, ps, etc.
  - Periodically collects resource usage data (e.g., every 5 seconds).
- Periodically sends resource usage data over the **network** to the **server**.

---

Functionality: `Python`, `psutil` OR `Bash` (top, ps, etc.), `socket`

### Network

- Connection between **client** (local PC) and **server** (Docker).
- **Client**(s) can communicate with the **server** through communication with the container.
- TCP/IP sockets or HTTP/HTTPS.

---

Functionality: `TCP` / `HTTP(S)`

### Server application

- Runs on Docker.
- **Server** receives resource data from multiple **clients**.
- **Server** stores received data in SQLite database for further processing.
- Contains a web-based interface to display visualized data.

---

Functionality: `SQLite`, `sqlite3`, `Flask` (visualization)

### Visualization

- Visualization using charts/graphs based on SQLite data.
  - Using gnuplot/chart.js, for example.
- Occurs on the **Server**.

---

Functionality: `Flask`, `gnuplot`, `chart.js`

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

