@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    await message.reply("Sleepy-LeechBot aktif ✅ Siap menerima perintah.")
