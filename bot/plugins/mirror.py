from pyrogram import filters
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
