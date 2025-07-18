import asyncio
from pyrogram import idle
from bot.core.mltb_client import TgClient

async def main():
    await TgClient.start_bot()
    await idle()  # biar bot standby menunggu pesan masuk

if __name__ == "__main__":
    asyncio.run(main())
