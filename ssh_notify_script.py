import logging
import traceback
import requests as req
from data.config import TOKEN, ADMINS, AUTH_LOG

def find_last_entries():
    file = open(AUTH_LOG, 'r')
    data = file.readlines()
    file.close()
    return [data[-1], data[-2], data[-3], data[-4], data[-5]]

def notify_text():
    try:
        lst = find_last_entries()
        text1 = '🐧 Обнаружена успешная авторизация на сервере по SSH!\nПоследние 5 записей:\n'
        for i in lst:
            text1 += f'▶ {i}'
        return text1
    except Exception as ex:
        logging.exception(ex)
        traceback.format_exc()
        return ex

if __name__ == '__main__':
    for admin in ADMINS:
        res = req.get(url=f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={admin}&text={notify_text()}')
