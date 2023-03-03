from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('memory', '(free -h) память сервера'),
        types.BotCommand('storage', '(df -hT) разделы дисков'),
        types.BotCommand('cpu', '(top -d) использование процессора'),
        types.BotCommand('status', '(systemctl status) состояние службы'),
    ])