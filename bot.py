app = web.AppRunner(await web_server())

        await app.setup()

        bind_address = "0.0.0.0"

        await web.TCPSite(app, bind_address, PORT).start()
