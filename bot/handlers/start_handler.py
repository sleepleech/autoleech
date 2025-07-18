from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    await message.reply_text(
        f"Halo {message.from_user.first_name}! 👋\n\n"
        "Ini adalah Sleepy-LeechBot, siap membantumu!"
    )
