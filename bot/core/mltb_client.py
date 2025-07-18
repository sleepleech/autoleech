import os
from pyrogram import Client

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
        print("Menyalakan Sleepy-LeechBot...")
        await cls.bot.start()
        me = await cls.bot.get_me()
        print(f"Bot aktif sebagai @{me.username}")
        await idle()
