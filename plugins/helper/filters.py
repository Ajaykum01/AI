from pyrogram import filters
from info import ADMINS  # make sure ADMINS list exists in your info.py

def is_admin():
    async def func(flt, client, message):
        # Check if user is admin (from ADMINS in info.py)
        if message.from_user:
            return message.from_user.id in ADMINS
        return False

    return filters.create(func)
