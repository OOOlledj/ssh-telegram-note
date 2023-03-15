import logging
from aiogram import Dispatcher
from aiogram import types
from data.config import ADMINS
from .db_logger import log_command


async def check_admin(message: types.Message):
    '''Проверить, является ли пользователь администратором сервера'''
    log_command(user_id=message.from_user.id, command=message.text)
    if str(message.from_user.id) in ADMINS:
        return True
    else: # неизвестные не могут получить доступ к выводу диагностических комманд
        await message.answer(f'У вас нет прав на выполнение этой команды!' )
        return False
