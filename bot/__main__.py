import asyncio
from bot.core.mltb_client import TgClient
import bot.handlers  # Pastikan file handler-nya benar

async def main():
    print("Menyalakan Sleepy-LeechBot...")
    await TgClient.start_bot()

if __name__ == "__main__":
    asyncio.run(main())
