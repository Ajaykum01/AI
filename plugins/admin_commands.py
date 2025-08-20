from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from helpers.filters import is_admin   # make sure you have this helper

# ---------- SETLINK ----------
@Client.on_message(filters.command("setlink") & is_admin())
async def setlink_handler(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "❌ Please provide a link.\n\nUsage: `/setlink <url>`",
            quote=True
        )

    link = message.command[1]
    # TODO: save link into DB if you want
    await message.reply_text(f"✅ Link has been set to:\n{link}", quote=True)


# ---------- BAN ----------
@Client.on_message(filters.command("ban") & is_admin())
async def ban_handler(client, message):
    if not message.reply_to_message and len(message.command) < 2:
        return await message.reply_text("Reply to a user or mention username to ban ❌", quote=True)

    user_id = message.reply_to_message.from_user.id if message.reply_to_message else message.command[1]

    try:
        await client.kick_chat_member(message.chat.id, user_id)
        await message.reply_text(f"✅ Banned {user_id}", quote=True)
    except Exception as e:
        await message.reply_text(f"❌ Error: {e}", quote=True)


# ---------- UNBAN ----------
@Client.on_message(filters.command("unban") & is_admin())
async def unban_handler(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: `/unban <user_id or @username>` ❌", quote=True)

    user_id = message.command[1]

    try:
        await client.unban_chat_member(message.chat.id, user_id)
        await message.reply_text(f"✅ Unbanned {user_id}", quote=True)
    except Exception as e:
        await message.reply_text(f"❌ Error: {e}", quote=True)


# ---------- MUTE ----------
@Client.on_message(filters.command("mute") & is_admin())
async def mute_handler(client, message):
    if not message.reply_to_message and len(message.command) < 2:
        return await message.reply_text("Reply to a user or mention username to mute ❌", quote=True)

    user_id = message.reply_to_message.from_user.id if message.reply_to_message else message.command[1]

    try:
        await client.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user_id,
            permissions=ChatPermissions(can_send_messages=False)
        )
        await message.reply_text(f"🔇 Muted {user_id}", quote=True)
    except Exception as e:
        await message.reply_text(f"❌ Error: {e}", quote=True)


# ---------- UNMUTE ----------
@Client.on_message(filters.command("unmute") & is_admin())
async def unmute_handler(client, message):
    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply_text("Usage: `/unmute <user_id>` ❌", quote=True)

    user_id = message.reply_to_message.from_user.id if message.reply_to_message else message.command[1]

    try:
        await client.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user_id,
            permissions=ChatPermissions(can_send_messages=True,
                                        can_send_media_messages=True,
                                        can_send_other_messages=True,
                                        can_add_web_page_previews=True)
        )
        await message.reply_text(f"🔊 Unmuted {user_id}", quote=True)
    except Exception as e:
        await message.reply_text(f"❌ Error: {e}", quote=True)
