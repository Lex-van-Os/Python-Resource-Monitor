import asyncio
import logging
import json

logger = logging.getLogger(__name__)

HOST = "0.0.0.0"
PORT = 8080


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
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
                logger.info(
                    f"Timestamp: {monitor_metrics['timestamp']!r} - Processes: {monitor_metrics['processes']!r} - CPU usage: {monitor_metrics['cpuUsage']!r} - Memory usage: {monitor_metrics['memoryUsage']!r} from {address}:{port}")
            except KeyError:
                logger.error("KeyError: key could not be found in metrics")
                continue

    logger.info("Closing writer")
    writer.close()
    await writer.wait_closed()


async def start_server() -> None:
    while True:
        server = await asyncio.start_server(handle_client, HOST, PORT)

        logger.info("Retrieving new socket connection")
        addr = server.sockets[0].getsockname()
        logger.info(f"Client connected on {addr}")

        async with server:
            await server.serve_forever()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.new_event_loop()

    try:
        loop.run_until_complete(start_server())
    except KeyboardInterrupt:
        logger.info("Program interrupted")
    finally:
        loop.close()
