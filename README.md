### Описание:
Когда происходит авторизация по SSH бот отправляет в телеграм сообщение с 5-ю последними записями из /var/log/auth.log

![alt text](https://i.ibb.co/kgVSgDg/terminal.png)

![alt text](https://i.ibb.co/sJDGwHF/tg.png)

### Установка ssh-notifier:
1. установить requirements.txt;
2. поместите файл <span style="color:red">sshrc</span> в <span style="color:red">/etc/ssh/sshrc</span>;
3. создайтей файл для конфигурации <span style="color:red">config.py</span> в папке "data", укажите переменные:
   - <span style="color:blue">TOKEN</span> = 'Токен бота';
   - <span style="color:blue">ADMINS</span> = ['tg-user-id-1', 'tg-user-id-2', ... ];
   - <span style="color:blue">AUTH_LOG</span> = '/var/log/auth.log';
4. создайте переменную окружения <span style="color:red">$project_path</span> в которой записан путь к проекту;
5. расшарьте пользователю права на чтение auth.log. Я использовал <span style="color:green">/usr/sbin/usermod -a -G adm ooolledj</span>;
6. Для тестирования откройте сессию в терминале (<span style="color:green">$ ssh 127.0.0.1</span>).

### Можно запустить основного бота (позднее сделаю файл сервиса) через app.py. Боту можно отправлять сообщения в телеграме и получать диагностическую информацию:###
1. /memory - "free -h";
2. /storage - "df -hT";
3. /cpu - "top -d | head -n 15" (Этого вывода, думаю, достаточно)
4. /status - "systemctl status", возвращает файл
5. /network - "ifconfig", возвращает файл
6. /uptime - "uptime"

Напоминаю, не забудьте записать id своего аккаунта в переменную ADMINS в *data/config.py*

### Использование
Authorize on host as any user and wait for telegram message, or use commands in Telegram bot to retrieve diagnostic info.
### Проблемы
~~До этого я использовал вызов aiogram, в котором при завершении программы выводится сообщение "Goodbye!", которое невозможно "заглушить"~~
