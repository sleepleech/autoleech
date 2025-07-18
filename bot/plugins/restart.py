import os
import sys
import asyncio
from pyrogram import filters
from pyrogram.types import Message
from bot import MLTBBot, OWNER_ID

@MLTBBot.on_message(filters.command("restart") & filters.user(OWNER_ID))
async def restart_bot(_, message: Message):
    await message.reply("♻️ Restarting bot...")
    await asyncio.sleep(1)
    os.execv(sys.executable, [sys.executable] + sys.argv)
