import logging
import sys
from aiogram import Bot, Dispatcher, executor
from config import TOKEN, ADMINS, AUTH_LOG
# TOKEN = 'TG BOT TOKEN'
# ADMINS = ['tg id 1', 'tg id 2', ... ]
# AUTH_LOG = '/var/log/auth.log'

def find_last_entries():
    file = open(AUTH_LOG, 'r')
    data = file.readlines()
    file.close()
    return [data[-1], data[-2], data[-3]]

async def notify_admins (dp: Dispatcher):
    for admin in ADMINS:
        try:
            lst = find_last_entries()
            text1 = '🐧 Обнаружена успешная авторизация на сервере по SSH!\nПоследние 3 записи:\n'
            for i in lst:
                text1 += f'▶ {i}'
            await dp.bot.send_message(chat_id=admin, text=text1)
        except Exception as err:
            logging.exception(err)

async def on_startup(dp):
    print('Server notified admins about successful authorization!')
    await notify_admins(dp)
    sys.exit(0)

if __name__ == "__main__":
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)
    executor.start_polling(dispatcher=dp,on_startup=(on_startup,))
