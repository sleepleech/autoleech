import asyncio
from bot.core.mltb_client import TgClient
import bot.handlers  # Pastikan folder handlers memiliki file _init_.py atau handler.py

async def main():
    print("Menyalakan Sleepy-LeechBot...")
    await TgClient.start_bot()

if __name__ == "_main_":
    asyncio.run(main())
