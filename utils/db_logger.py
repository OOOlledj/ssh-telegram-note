import sqlite3
from datetime import datetime

db_file = 'bot_log.db'

def open_connection():
    '''Открыть соединение с файлом БД'''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as ex:
        print(ex)
    return conn

def create_log_table():
    '''Создать таблицы в файле.
    Только при запуске бота!!!'''
    conn = open_connection()
    table = """CREATE TABLE IF NOT EXISTS bot_commands (
        id integer PRIMARY KEY AUTOINCREMENT,
        date text,
        user_id text,
        bot_cmd text); 
    """
    try:
        cursor = conn.cursor()
        cursor.execute(table)
        conn.commit()
    except sqlite3.Error as ex:
        print(ex)
    finally:
        conn.close()

def log_command(user_id, command):
    '''Записать в таблицу использование команды бота'''
    conn = open_connection()
    insert = f'INSERT INTO bot_commands (date, user_id, bot_cmd) VALUES(?,?,?)'
    data = (datetime.now().strftime("%d.%m.%Y %H:%M:%S"), user_id, command)
    try:
        cursor = conn.cursor()
        cursor.execute(insert, data)
        conn.commit()
        print(data)
    except sqlite3.Error as ex:
        print(ex)
    finally:
        conn.close()
