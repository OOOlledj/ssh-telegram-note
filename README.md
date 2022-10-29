### Description
This bot will send you telegram message with last 3 entries of /var/log/auth.log.

![alt text](https://i.ibb.co/tHJq7KW/ssh.png)

![alt text](https://i.ibb.co/kgQ8bZ9/tg.png)

### Installation
1. install requirements.txt (<span style="color:green">pip install aiogram==2.22</span>);
2. put <span style="color:red">sshrc</span> to <span style="color:red">/etc/ssh/sshrc</span>;
3. create <span style="color:red">config.py</span> file and provide variables:
   - <span style="color:blue">TOKEN</span> = 'TG BOT TOKEN';
   - <span style="color:blue">ADMINS</span> = ['tg-user-id-1', 'tg-user-id-2', ... ];
   - <span style="color:blue">AUTH_LOG</span> = '/var/log/auth.log';
4. provede environment <span style="color:red">$project_path</span> with project location;
5. test authorization via terminal (<span style="color:green">$ ssh 127.0.0.1</span>).

### Usage

Authorize on host as any user and wait for telegram message.

### Issues

- When script exit, it sends to the terminal message 'Goodbye!'. It's aiogram library feature, i did not found solution to suppress the output.