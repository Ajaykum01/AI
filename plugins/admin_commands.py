from pyrogram import filters
from pyrogram.types import Message
from info import ADMINS

# Temporary in-memory storage; replace with DB storage if needed
from utils import temp
temp.SETTINGS = {}

def is_admin():
    return filters.user(ADMINS)

@app.on_message(filters.command("setlink") & is_admin())
async def set_link_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage: `/setlink <your_link>`", quote=True)
        return
    link = message.text.split(None, 1)[1]
    temp.SETTINGS["LINK"] = link
    await message.reply_text(f"✅ Link set to:\n`{link}`", quote=True)

@app.on_message(filters.command("setapi") & is_admin())
async def set_api_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage: `/setapi <your_api>`", quote=True)
        return
    api = message.text.split(None, 1)[1]
    temp.SETTINGS["API"] = api
    await message.reply_text(f"✅ API set to:\n`{api}`", quote=True)
