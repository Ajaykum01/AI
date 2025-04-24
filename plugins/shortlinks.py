from pyrogram import filters
from pyrogram.types import Message
from your_bot import app, db  # Adjust the import based on your project structure
from config import ADMINS

@app.on_message(filters.command("seturl") & filters.user(ADMINS))
async def set_url(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("Usage: /seturl yourdomain.com (without https://)")
    url = message.command[1]
    await db.bot_config.update_one({"_id": "bot_config"}, {"$set": {"shortener_url": url}}, upsert=True)
    await message.reply(f"Shortener domain set to: `{url}`")

@app.on_message(filters.command("setapi") & filters.user(ADMINS))
async def set_api(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("Usage: /setapi your_api_key")
    api_key = message.command[1]
    await db.bot_config.update_one({"_id": "bot_config"}, {"$set": {"shortener_api": api_key}}, upsert=True)
    await message.reply("Shortener API key saved.")
