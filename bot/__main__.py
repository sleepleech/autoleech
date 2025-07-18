import asyncio
from bot.core.mltb_client import TgClient

async def main():
    await asyncio.gather(
        TgClient.start_bot()
    )

if _name_ == "__main__":
    asyncio.run(main())
