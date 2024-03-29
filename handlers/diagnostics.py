'''Обработка диагностических комманд'''

import traceback

from aiogram import types
from loader import dp
from utils.check_admin import check_admin
from utils.linux_commands import linux_command_ex, create_temp_file, remove_temp_file


@dp.message_handler(text='/memory')
async def memory(message: types.Message):
    '''Память, free -h'''
    if await check_admin(message):
        text = linux_command_ex('free -h')
        await message.answer(text)
    else:
        pass


@dp.message_handler(text='/cpu')
async def cpu(message: types.Message):
    '''Процессор, top -b -n 1 | head -n 15'''
    if await check_admin(message):
        text = linux_command_ex('top -b -n 1 | head -n 15')
        await message.answer(text)
    else:
        pass


@dp.message_handler(text='/storage')
async def storage(message: types.Message):
    '''Диск, df -hT'''
    if await check_admin(message):
        text = linux_command_ex('df -hT')
        await message.answer(text)
    else:
        pass


@dp.message_handler(text='/status')
async def sys_status(message: types.Message):
    '''Службы, systemctl status
       Возвращает файл'''
    if await check_admin(message):
        text = linux_command_ex('systemctl status --no-pager')
        temp_file = create_temp_file(data=text, prefix='systemctl-')
        if temp_file: # если временный файл удалось создать и вернулось имя файла
            file = open(temp_file, 'rb')
            await message.answer_document(file)
            file.close()
        else:
            await message.answer('Не удалось отправить файл с диагностикой!')
        remove_temp_file(temp_file)


@dp.message_handler(text='/network')
async def network(message: types.Message):
    '''Сетевые интерфейсы, ifconfig или ip addr
        Возвращает файл'''
    if await check_admin(message):
        text = linux_command_ex('ifconfig')
        if text=='': # если команды нет, можно попробовать ip
            text = text = linux_command_ex('ip addr')
        temp_file = create_temp_file(data=text, prefix='network-')
        if temp_file:
            file = open(temp_file, 'rb')
            await message.answer_document(file)
            file.close()
        else:
            await message.answer('Не удалось отправить файл с диагностикой!')
        remove_temp_file(temp_file)
    else:
        pass


@dp.message_handler(text='/uptime')
async def memory(message: types.Message):
    '''Время работы, uptime'''
    if await check_admin(message):
        text = linux_command_ex('uptime')
        await message.answer(text)
    else:
        pass
