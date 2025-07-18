from pyrogram import filters
from pyrogram.types import Message
from bot import MLTBBot

@MLTBBot.on_message(filters.command("start") & filters.private)
async def start_handler(_, message: Message):
    await message.reply_text(
        f"Halo {message.from_user.first_name}!\n\n"
        "Saya adalah bot Mirror-Leech All-In-One 🔄📤\n\n"
        "Ketik /help untuk melihat semua fitur!"
    )
