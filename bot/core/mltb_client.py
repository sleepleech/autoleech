import os
from pyrogram import Client, idle

# ⬅️ INI WAJIB AGAR HANDLER KELOAD
import bot.handlers

class TgClient:
    bot = Client(
        "bot",
        bot_token=os.environ.get("BOT_TOKEN"),
        api_id=int(os.environ.get("API_ID")),
        api_hash=os.environ.get("API_HASH"),
        workdir="session"
    )

    @classmethod
    async def start_bot(cls):
        print("[1] Mulai start_bot()...")
        await cls.bot.start()  # ⬅️ Harus dipanggil setelah import handler
        print("[2] Bot sudah start()")
        me = await cls.bot.get_me()
        print(f"[3] Bot aktif sebagai @{me.username}")
        print("[4] Masuk idle mode...")
        await idle()
        print("[5] Idle selesai, keluar.")
