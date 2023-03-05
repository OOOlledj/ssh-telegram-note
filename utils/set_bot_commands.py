from aiogram import types

async def set_default_commands(dp):
    '''команды из меню'''
    await dp.bot.set_my_commands([
        types.BotCommand('cpu', '(top -d) использование процессора'),
        types.BotCommand('memory', '(free -h) память сервера'),
        types.BotCommand('storage', '(df -hT) разделы дисков'),
        types.BotCommand('uptime', '(uptime) время работы'),
        types.BotCommand('status', '(systemctl status) состояние служб'),
        types.BotCommand('network', '(ifconfig) сетевые интерфейсы'),
    ])