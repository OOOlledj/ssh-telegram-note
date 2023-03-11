'''Команды для работы с файловой системой'''

import traceback
import os

from aiogram import types
from loader import dp
from utils.check_admin import check_admin
from utils.linux_commands import linux_command_ex, create_temp_file, remove_temp_file


@dp.message_handler(commands=['getfl'])
async def get_server_file(message: types.Message):
    '''Прочитать и отправить пользователю файл'''
    if await check_admin(message):
        filepath = message.get_args()
        try:
            if filepath == '':
                raise FileNotFoundError('Не указан путь к директории или файлу')
            file = open(filepath, 'rb')
            await message.answer_document(file)
            file.close()
        except FileNotFoundError as ex:
            await message.answer(f'Не удалось найти файл или директорию "{filepath}"\n{ex}')
        except PermissionError as ex:
            await message.answer(f'Нет доступа к файлу или директории "{filepath}"\n{ex}')
        except IsADirectoryError as ex:
            await message.answer(f'Не могу скачать директорию "{filepath}"\n{ex}')
        except Exception:
            await message.answer(f'Что-то пошло не так:\n{traceback.format_exc()}')


@dp.message_handler(commands=['ls', 'lsa'])
async def get_dir_ls(message: types.Message):
    '''ls -lh(a) - перечислить файлы в директории'''
    if await check_admin(message):
        filepath = message.get_args()
        try:
            if filepath == '':
                raise FileNotFoundError('Не указан путь к директории или файлу')
            if message.get_command() == '/ls':
                text = linux_command_ex(f'ls -lh {filepath}')
            if message.get_command() == '/lsa':
                text = linux_command_ex(f'ls -alh {filepath}')
            if len(text) < 2048:
                await message.answer(text)
            else:
                temp_file = create_temp_file(data=text, prefix='ls-')
                if temp_file:  # если временный файл удалось создать и вернулось имя файла
                    file = open(temp_file, 'rb')
                    await message.answer_document(file, caption='Размер ответа слишком большой, результат записан в файл')
                    file.close()
                remove_temp_file(temp_file)
        except FileNotFoundError as ex:
            await message.answer(f'Не удалось найти файл или директорию "{filepath}"\n{ex}')
        except PermissionError as ex:
            await message.answer(f'Нет доступа к файлу или директории "{filepath}"\n{ex}')
        except Exception:
            await message.answer(f'Что-то пошло не так:\n{traceback.format_exc()}')