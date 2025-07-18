from pyrogram import filters
from pyrogram.types import Message
from bot import MLTBBot

@MLTBBot.on_message(filters.command("status") & filters.private)
async def status_handler(_, message: Message):
    await message.reply("📊 Bot sedang idle.\nTidak ada tugas aktif.")
