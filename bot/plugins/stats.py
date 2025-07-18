from pyrogram import filters
from pyrogram.types import Message
from bot import MLTBBot

@MLTBBot.on_message(filters.command("stats") & filters.private)
async def stats_handler(_, message: Message):
    await message.reply(
        "📈 Statistik Penggunaan:\n"
        "- Total Tugas: 0\n"
        "- Total Data Diunduh: 0MB\n"
        "- User Aktif: 1 (Owner)"
    )
