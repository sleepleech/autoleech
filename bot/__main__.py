import asyncio
from bot.core.mltb_client import TgClient

async def main():
    await asyncio.gather(
        TgClient.start_bot()
    )

if _name_ == "_main_":
    asyncio.run(main())
