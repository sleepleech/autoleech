[16:41, 7/18/2025] Aq: from pyrogram import filters
from pyrogram.types import Message
from bot import MLTBBot

@MLTBBot.on_message(filters.command("mirror") & filters.private)
async def mirror_handler(_, message: Message):
    if message.reply_to_message and message.reply_to_message.text:
        link = message.reply_to_message.text.strip()
    else:
        parts = message.text.split(maxsplit=1)
        if len(parts) == 2:
            link = parts[1]
        else:
            await message.reply("Berikan link yang ingin di-mirror.")
            return

    await message.reply(f"🔄 Memproses link:\n{link}\n\n(Contoh stub: belum upload ke GDrive)")
[16:42, 7/18/2025] Aq: bot/plugins/leech.py
[16:42, 7/18/2025] Aq: from pyrogram import filters
from pyrogram.types import Message
from bot import MLTBBot
import aiohttp
import os

@MLTBBot.on_message(filters.command("leech") & filters.private)
async def leech_handler(_, message: Message):
    if message.reply_to_message and message.reply_to_message.text:
        url = message.reply_to_message.text.strip()
    else:
        parts = message.text.split(maxsplit=1)
        if len(parts) == 2:
            url = parts[1]
        else:
            await message.reply("Berikan link yang ingin diunduh.")
            return

    file_name = url.split("/")[-1]
    await message.reply(f"📥 Mengunduh: {file_name}")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                with open(file_name, "wb") as f:
                    f.write(await resp.read())

        await message.reply_document(file_name)
        os.remove(file_name)

    except Exception as e:
        await message.reply(f"❌ Gagal:\n{e}")
