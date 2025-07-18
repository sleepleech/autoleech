from pyrogram import filters
from pyrogram.types import Message
from bot.core.client_instance import bot

@bot.on_message(filters.command("start") & filters.private)
async def start_command(client, message: Message):
    await message.reply_text("Halo! Bot aktif 👋")
