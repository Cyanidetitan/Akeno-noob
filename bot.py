import asyncio
from aiohttp import web

async def run_app():
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    PORT = 8080  # Replace with the desired port number
    await web.TCPSite(app, bind_address, PORT).start()

asyncio.run(run_app())
 

