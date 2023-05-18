



from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)

async def root_route_handler(request):

    return web.json_response("AnimeDrobe")

app = web.AppRunner(await web_server())

        await app.setup()

        bind_address = "0.0.0.0"

        await web.TCPSite(app, bind_address, PORT).start()
