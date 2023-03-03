from aiogram import types
from loader import dp
from utils.check_admin import check_admin

@dp.message_handler(text='/memory')
async def memory(message: types.Message):
    '''free -h'''
    if await check_admin(message):
        await message.answer(f'memory' )
    else:
        pass

@dp.message_handler(text='/cpu')
async def cpu(message: types.Message):
    '''top -b -n 1 | head -n 15 > toptop.log'''
    if await check_admin(message):
        await message.answer(f'cpu' )
    else:
        pass

@dp.message_handler(text='/storage')
async def storage(message: types.Message):
    '''df -hT'''
    if await check_admin(message):
        await message.answer(f'storage' )
    else:
        pass

@dp.message_handler(text='/status')
async def sysstatus(message: types.Message):
    '''systemctl status <service name>'''
    if await check_admin(message):
        await message.answer(f'service status: test' )
    else:
        pass