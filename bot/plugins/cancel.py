from pyrogram import filters
from pyrogram.types import Message
from bot import MLTBBot

@MLTBBot.on_message(filters.command("cancel") & filters.private)
async def cancel_handler(_, message: Message):
    await message.reply("🚫 Tidak ada tugas yang sedang berjalan.")
