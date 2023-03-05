'''Команды для openvpn server'''

import traceback

from aiogram import types
from loader import dp
from utils.check_admin import check_admin
from utils.linux_commands import linux_command_ex, create_temp_file, remove_temp_file


@dp.message_handler(text='/ovpn',)
async def ovpn_status(message: types.Message):
    '''cat /var/log/openvpn/status.log'''
    args = message.get_args()
    if args!='':
        await message.answer(args)

    if await check_admin(message):
        text = linux_command_ex('cat /var/log/openvpn/status.log')
        if text=='':
            text = '/var/log/openvpn.log is empty!'
        await message.answer(text)
    else:
        pass
