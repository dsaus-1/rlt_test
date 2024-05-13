import os, asyncio

from src.tg.config import dp, bot

dir_path = os.path.dirname(os.path.realpath(__file__))

async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())