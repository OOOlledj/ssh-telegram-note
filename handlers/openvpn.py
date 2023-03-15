'''Команды для openvpn server'''

import traceback

from aiogram import types
from loader import dp
from utils.check_admin import check_admin
from utils.linux_commands import linux_command_ex, create_temp_file, remove_temp_file


@dp.message_handler(text='/ovpn_conn',)
async def ovpn_status(message: types.Message):
    '''cat /var/log/openvpn/status.log'''
    if await check_admin(message):
        args = message.get_args()
        if args != '':
            await message.answer(args)
        text = linux_command_ex('cat /var/log/openvpn/status.log')
        if text=='':
            text = '/var/log/openvpn.log is empty!'
        await message.answer(text)
    else:
        pass


@dp.message_handler(text='/ovpn_log',)
async def ovpn_log(message: types.Message):
    '''cat /var/log/openvpn/status.log'''
    if await check_admin(message):
        args = message.get_args()
        if args != '':
            await message.answer(args)
        text = linux_command_ex('cat /var/log/syslog | grep vpn')
        temp_file = create_temp_file(text, prefix='syslog-ovpn-')
        file = open(temp_file, 'rb')
        await message.answer_document(file)
        file.close()
        remove_temp_file(temp_file)
    else:
        pass