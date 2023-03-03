import logging
from aiogram import Dispatcher
from aiogram import types
from data.config import ADMINS

async def check_admin(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        return True
    else:
        await message.answer(f'У вас нет прав на выполнение этой команды!' )
        return False