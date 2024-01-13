import asyncio
import logging
import json
import os
from uuid import uuid4
from influx_client import MonitorInfluxClient
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from monitor_metrics import MonitorMetrics
from user import User

logger = logging.getLogger(__name__)

HOST = os.getenv("SERVER_HOST", "0.0.0.0")
PORT = os.getenv("SERVER_PORT", 8080)

# Retrieve configuration for the InfuxDB client
influx_url = os.getenv("INFLUX_URL", "http://localhost:8086")
influx_token = os.getenv("INFLUX_TOKEN", "my-token")
influx_org = os.getenv("INFLUX_ORG", "my-org")
influx_bucket = os.getenv("INFLUX_BUCKET", "my-bucket")
influx_bucket_auth = os.getenv("INFLUX_BUCKET_AUTH", "my-token")

# Keep track of connected users
users = []


async def track_ip_address(ip_address: str) -> None:
    try:
        user = next(
            (user for user in users if user.ip_address == ip_address), None)
        if user is None:
            new_user = User(ip_address, str(uuid4())[:5])
            users.append(new_user)
    except Exception as e:
        logger.error(f"Error occurred while tracking IP address: {e}")


async def initialize_monitor_client() -> MonitorInfluxClient:
    monitorInfluxClient = MonitorInfluxClient(
        influx_url, influx_token, influx_org, influx_bucket)
    await monitorInfluxClient.initialize()
    return monitorInfluxClient


async def handle_client(monitorInfluxClient: MonitorInfluxClient, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    logger.info("New client connected")
    user_uid = str(uuid4())[:5]

    # Maybe this method is not necessary
    # await track_ip_address(writer.get_extra_info("peername"))
    data = None

    while True:
        try:
            data = await reader.read(1024)
        except asyncio.IncompleteReadError:
            logger.info("Client disconnected")
            break

        if not data:
            logger.info("Client disconnected")
            break
        else:
            msg = data.decode()
            monitor_metrics = json.loads(msg)
            address, port = writer.get_extra_info("peername")

            try:
                timestamp = str(monitor_metrics["timestamp"])
                processes = int(monitor_metrics["processes"])
                cpu_usage = float(monitor_metrics["cpuUsage"])
                memory_usage = int(monitor_metrics["memoryUsage"])

                converted_metrics = MonitorMetrics(
                    timestamp, processes, cpu_usage, memory_usage)

                logger.info(f"Timestamp: {converted_metrics.timestamp!r} - Processes: {converted_metrics.processes!r} - CPU usage: {converted_metrics.cpu_usage!r} - Memory usage: {converted_metrics.memory_usage!r} - User: {user_uid} from {address}:{port}")

                await monitorInfluxClient.write_monitor_metrics(
                    converted_metrics, user_uid)

            except KeyError:
                logger.error("KeyError: key could not be found in metrics")
                continue

    logger.info("Closing writer")
    writer.close()
    await writer.wait_closed()


async def start_server(monitorInfluxClient) -> None:
    async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        await handle_client(monitorInfluxClient, reader, writer)

    while True:
        server = await asyncio.start_server(handler, HOST, PORT)

        logger.info("Retrieving new socket connection")
        addr = server.sockets[0].getsockname()
        logger.info(f"Client connected on {addr}")

        async with server:
            await server.serve_forever()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.new_event_loop()

    try:
        monitorInfluxClient = loop.run_until_complete(
            initialize_monitor_client())
        loop.run_until_complete(start_server(monitorInfluxClient))
    except KeyboardInterrupt:
        logger.info("Program interrupted")
    finally:
        loop.run_until_complete(monitorInfluxClient.close())
        loop.close()
