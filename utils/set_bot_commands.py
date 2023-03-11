from aiogram import types

async def set_default_commands(dp):
    '''команды из меню'''
    await dp.bot.set_my_commands([
        #types.BotCommand('','')
        types.BotCommand('cpu', '(top -d) использование процессора'),
        types.BotCommand('memory', '(free -h) память сервера'),
        types.BotCommand('storage', '(df -hT) разделы дисков'),
        types.BotCommand('uptime', '(uptime) время работы'),
        types.BotCommand('status', '(systemctl status) состояние служб'),
        types.BotCommand('network', '(ifconfig) сетевые интерфейсы'),
        types.BotCommand('ovpn_conn', 'Подключенные пользователи'),
        types.BotCommand('ovpn_log', 'Логи сервера OpenVPN'),
        types.BotCommand('getfl', 'Скачать файл'),
        types.BotCommand('ls', 'Файлы в директории'),
        types.BotCommand('lsa', 'Файлы в диретории (скрытые)')

    ])