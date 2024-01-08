import asyncio
import logging

logger = logging.getLogger(__name__)

HOST = "127.0.0.1"
PORT = 43256

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    logger.info("Client connected")
    data = None

    while True:
        try:
            data = await reader.read(1024)
        except asyncio.IncompleteReadError:
            logger.info("Client disconnected")
            break

        if not data:
            break
        else:
            msg = data.decode()
            address, port = writer.get_extra_info("peername")
            logger.info(f"Received {msg!r} from {address}:{port}")

    writer.close()
    await writer.wait_closed()

async def start_server() -> None:
    print("Starting server")
    while True:
        server = await asyncio.start_server(handle_client, HOST, PORT)

        async with server:
            await server.serve_forever()

if __name__ == "__main__":
    print("Hello world!")
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.new_event_loop()

    try:
        loop.run_until_complete(start_server())
    except KeyboardInterrupt:
        logger.info("Program interrupted")
    finally:
        loop.close()