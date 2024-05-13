from aiogram import Router
import asyncio

from src.services import get_data
from src.db.config import db, DB_COLLECTION

router = Router()


@router.message()
async def pars_data(message):
    dict_message = eval(message.text)
    print(dict_message)
    answer = await get_data(db, DB_COLLECTION, dict_message['dt_from'], dict_message['dt_upto'], dict_message['group_type'])
    await message.answer(f'{answer}')
