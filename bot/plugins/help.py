from pyrogram import filters
from pyrogram.types import Message
from bot import MLTBBot

HELP_TEXT = """
*🛠 Fitur Mirror-Leech Bot:*

/start - Mulai bot
/help - Bantuan & info
/mirror [link|reply] - Mirror ke GDrive
/leech [link|reply] - Leech ke Telegram
/status - Status proses
/cancel - Batalkan proses
/stats - Statistik bot
"""

@MLTBBot.on_message(filters.command("help") & filters.private)
async def help_handler(_, message: Message):
    await message.reply_text(HELP_TEXT)
