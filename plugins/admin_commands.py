from pyrogram import Client, filters
from helpers.filters import is_admin   # only if you created is_admin()

@Client.on_message(filters.command("setlink") & is_admin())
async def setlink_handler(client, message):
    # your custom logic
    await message.reply_text("✅ Setlink command received")
