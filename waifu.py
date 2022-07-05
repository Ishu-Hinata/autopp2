import time
import os
import sys
import urllib
import requests

from bs4 import BeautifulSoup
from asyncio import get_event_loop
from pyrogram import (
    Client,
    filters,
    idle,
)
from pyrogram.handlers import MessageHandler


HEROKU = bool(os.environ.get("HEROKU", False))
try:
    if HEROKU:
        APP_ID = int(os.environ.get("APP_ID"))
        API_HASH = str(os.environ.get("API_HASH"))
        STRING_SESSION = str(os.environ.get("STRING_SESSION"))
        DELAY = int(os.environ.get("DELAY"))
        BOT_LIST = int(x for x in os.environ.get("BOT_LIST").split())
    else:
        from config import config

        APP_ID = config.APP_ID
        API_HASH = config.API_HASH
        STRING_SESSION = config.STRING_SESSION
        DELAY = config.DELAY
        BOT_LIST = config.BOT_LIST
except Exception as e:
    print(e)
    print("One or more variables missing or have error. Exiting !")
    sys.exit(1)


waifu = Client(
    STRING_SESSION,
    api_id=APP_ID,
    api_hash=API_HASH,
)


opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]

@waifu.on_message(filters.regex(pattern="You've been offered a waifu trade!"))
async def trade(ub, message):
    await asyncio.sleep(30)
    await message.delete()
    
@waifu.on_message(filters.regex(pattern="rip, the waifu has run away already..."))
async def ran(ub, message):
    await asyncio.sleep(4)
    async for m in ub.search_messages(message.chat.id, query='A qt waifu appeared!', limit=1):
        await m.delete()
    await asyncio.sleep(20)
    await message.delete()
    
@waifu.on_message(filters.regex(pattern="rip, that's not quite right..."))
async def rip(ub, message):
    await asyncio.sleep(3)
    await message.delete()
    
@waifu.on_message(filters.regex(pattern="OwO you protecc'd"))
async def done(ub, message):
    await asyncio.sleep(4)
    async for m in ub.search_messages(message.chat.id, query='A qt waifu appeared!', limit=1):
        await m.delete()
    await asyncio.sleep(6)
    await message.delete()
    
@waifu.on_message(filters.regex(pattern="Top harems in"))
async def top(ub, message):
    await asyncio.sleep(60)
    await message.delete()
@waifu.on_message(filters.regex(pattern="kek that doesn't look right. Reply to someone like this:"))
async def rip(ub, message):
    await asyncio.sleep(3)
    await message.delete()

waifu.start()
