from Plugins.starter import start
from Plugins.anime import Anime
from Plugins.manga import Manga
from Plugins.nhentai import Nhentai
from config import bot
from bot import Bot
try:
    start()
    Anime()
    Manga()
    Nhentai()
    
except Exception as e:
    print(e)

bot.start()

bot.run_until_disconnected()


Bot().run()
