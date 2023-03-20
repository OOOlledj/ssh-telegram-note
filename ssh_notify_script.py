import logging
import traceback
import requests as req
from data.config import TOKEN, ADMINS, AUTH_LOG
from http import HTTPStatus


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


def tty_notification_message(status_code):
    print()
    if HTTPStatus.OK <= status_code <= HTTPStatus.IM_USED:
        print('Administrators will be notified about new SSH session via Telegram!')
    else:
        print('Admin notification error:')
        if status_code == HTTPStatus.BAD_REQUEST:
            print('400, BAD REQUEST')
        elif status_code == HTTPStatus.NOT_FOUND:
            print('404, NOT FOUND')
        elif status_code == HTTPStatus.UNAUTHORIZED:
            print('401, UNAUTHORIZED')
        elif status_code == HTTPStatus.FORBIDDEN:
            print('403, FORBIDDEN')
        elif status_code >= HTTPStatus.INTERNAL_SERVER_ERROR:
            print('status code >= 500, SERVER ERROR')
        # Другие ошибки - исключения в работе скрипта
        elif status_code == -1:
            print('Connect Timeout Error')
        elif status_code == -2:
            print('Unknown script error')
        else:
            print('Unknown HTTP error')
    print()


if __name__ == '__main__':
    status_code = -2
    for admin in ADMINS:
        try:
            status_code = req.get(url=f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={admin}&text={notify_text()}', timeout=(6, 6)).status_code
        except requests.ConnectTimeoutError:
            status_code = -1
        except Exception:
            pass  #  status_code = -2
    tty_notification_message(status_code)
