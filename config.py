import os
from telethon import TelegramClient

api_id = "10247139"
api_hash = "96b46175824223a33737657ab943fd6a"
bot_token = "5695907792:AAEwiocIydMIK0OtdqJIreH4RByXEMJ36u8"

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
