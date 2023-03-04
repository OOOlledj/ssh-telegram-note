from aiogram import types
from loader import dp
from utils.check_admin import check_admin
from utils.linux_commands import linux_command_ex, create_temp_file, remove_temp_file

@dp.message_handler(text='/memory')
async def memory(message: types.Message):
    '''free -h'''
    if await check_admin(message):
        text = linux_command_ex('free -h')
        await message.answer(text)
    else:
        pass

@dp.message_handler(text='/cpu')
async def cpu(message: types.Message):
    '''top -b -n 1 | head -n 15 > toptop.log'''
    if await check_admin(message):
        text = linux_command_ex('top -b -n 1 | head -n 15')
        await message.answer(text)
    else:
        pass

@dp.message_handler(text='/storage')
async def storage(message: types.Message):
    '''df -hT'''
    if await check_admin(message):
        text = linux_command_ex('df -hT')
        await message.answer(text)
    else:
        pass

@dp.message_handler(text='/status')
async def sysstatus(message: types.Message):
    '''systemctl status'''
    if await check_admin(message):
        SPLIT = 1024
        text = linux_command_ex('systemctl status --no-pager')
        temp_file = create_temp_file(data=text, prefix='systemctl-')
        if temp_file:
            file = open(temp_file, 'rb')
            await message.answer_document(file)
            file.close()
        else:
            await message.answer('Не удалось отправить файл, попробуйте позже')
        temp_remove = remove_temp_file(temp_file)
        # if temp_remove:
        #     pass
        # else:
        #     pass

@dp.message_handler(text='/network')
async def network(message: types.Message):
    '''ifconfig'''
    if await check_admin(message):
        text = linux_command_ex('ifconfig')
        temp_file = create_temp_file(data=text, prefix='network-')
        if temp_file:
            file = open(temp_file, 'rb')
            await message.answer_document(file)
            file.close()
        else:
            await message.answer('Не удалось отправить файл, попробуйте позже')
        temp_remove = remove_temp_file(temp_file)
    else:
        pass

@dp.message_handler(text='/uptime')
async def memory(message: types.Message):
    '''uptime'''
    if await check_admin(message):
        text = linux_command_ex('uptime')
        await message.answer(text)
    else:
        pass