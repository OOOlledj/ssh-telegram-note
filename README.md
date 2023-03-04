### Description
This bot will send you telegram message with last 5 entries of /var/log/auth.log.

![alt text](https://i.ibb.co/kgVSgDg/terminal.png)

![alt text](https://i.ibb.co/sJDGwHF/tg.png)

### Installation of ssh-notifier:
1. install requirements.txt;
2. put <span style="color:red">sshrc</span> to <span style="color:red">/etc/ssh/sshrc</span>;
3. create <span style="color:red">config.py</span> file in directory "data" and provide variables:
   - <span style="color:blue">TOKEN</span> = 'TG BOT TOKEN';
   - <span style="color:blue">ADMINS</span> = ['tg-user-id-1', 'tg-user-id-2', ... ];
   - <span style="color:blue">AUTH_LOG</span> = '/var/log/auth.log';
4. provide environment <span style="color:red">$project_path</span> with project location;
5. allow your user to read auth.log. I used <span style="color:green">/usr/sbin/usermod -a -G adm ooolledj</span>;
6. test authorization via terminal (<span style="color:green">$ ssh 127.0.0.1</span>).

### Also you can run bot on server (i'll write service file later) with app.py. After it you can send commands to bot and recieve diagnostic information: ###
1. /memory - "free -h";
2. /storage - "df -hT";
3. /cpu - "top -d | head -n 15" (i'm sure this is enough for now)
4. /status - "systemctl status", file with output
5. /network - "ifconfig", file with output
6. /uptime - "uptime"

commands will not work if you did not write your Telegram id to ADMINS variable in *config.py*

### Usage

Authorize on host as any user and wait for telegram message, or use commands in Telegram bot to retrieve diagnostic info.

### Issues

~~- When script exit, it sends to the terminal message 'Goodbye!'. It's aiogram library feature, i did not found solution to suppress the output.~~
