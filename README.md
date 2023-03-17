### Описание:
Когда происходит авторизация по SSH бот отправляет в телеграм сообщение с 5-ю последними записями из /var/log/auth.log

![alt text](https://i.ibb.co/kgVSgDg/terminal.png)

![alt text](https://i.ibb.co/sJDGwHF/tg.png)

### Установка ssh-notifier:
1. установить requirements.txt;
2. поместите файл <span style="color:red">sshrc</span> в <span style="color:red">/etc/ssh/sshrc</span> или добавьте в свой файл:
   - project_path=/home/ooolledj/ssh-telegram-note
   - python3 $project_path/ssh_notify_script.py
3. создайтей файл для конфигурации <span style="color:red">config.py</span> в папке "data", укажите переменные:
   - <span style="color:blue">TOKEN</span> = 'Токен бота';
   - <span style="color:blue">ADMINS</span> = ['tg-user-id-1', 'tg-user-id-2', ... ];
   - <span style="color:blue">AUTH_LOG</span> = '/var/log/auth.log';
4. создайте переменную окружения <span style="color:red">$project_path</span> в которой записан путь к проекту;
   - Или экспортируйте прямо в sshrc согласно пункту 2;
5. расшарьте пользователю права на чтение auth.log. Я использовал <span style="color:green">/usr/sbin/usermod -a -G adm ooolledj</span>;
6. Для тестирования откройте сессию в терминале (<span style="color:green">$ ssh 127.0.0.1</span>).

### Можно запустить основного бота ~~(позднее сделаю файл сервиса) через app.py~~ через systemctl. Для этого нужно поместить файл tgbot.service в папку /etc/systemd/system/
Соответственно, в файле нужно изменить под себя следующие опции:
User=<Ваш юзер>
Group=<Ваша группа>
WorkingDirectory=<Директория проекта>

### Боту можно отправлять сообщения в телеграме и получать диагностическую и другую информацию:
1. /memory - "free -h";
2. /storage - "df -hT";
3. /cpu - "top -d | head -n 15" (Этого вывода, думаю, достаточно)
4. /status - "systemctl status", возвращает файл
5. /network - "ifconfig", возвращает файл
6. /uptime - "uptime"
7. /ovpn_conn - пока только вывод текущих пользователей из /var/log/openvpn/status.log. Также нужно расшарить на чтение пользователю!!!
8. /ovpn_log - логи сервера с использованием grep vpn
9. /getfl - скачать файл с сервера (требует путь к файлу в качестве аргумента)
10. /ls (/lsa) - вывод файлов в указанной диретории (требует путь к файлу в качестве аргумента)

Напоминаю, не забудьте записать id своего аккаунта телеграм в переменную ADMINS в *data/config.py*

### Проблемы
~~До этого я использовал вызов aiogram, в котором при завершении программы выводится сообщение "Goodbye!", которое невозможно "заглушить"~~
