from dotenv import load_dotenv
import os, asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart

from src.tg.handlers import router


load_dotenv()

TOKEN = os.environ.get('BOT_TOKEN')
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
dp.include_router(router)


@dp.message(CommandStart())
async def command_start_handler(message):
    await message.answer(f"Добро пожаловать! Это тестовый бот)")


async def main() -> None:
    await dp.start_polling(bot)


