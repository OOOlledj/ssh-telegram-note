'''Команды, которые выполняются только на сервере'''

import os
import random
import traceback


def linux_command_ex(command):
    '''Выполнить команду в терминале на linux хосте'''
    try:
        stream = os.popen(f'{command}') # Отправить команду
        res = stream.read()             # Прочесть вывод
        return res
    except:
        print('Error while running linux command')
        traceback.format_exc()
        return False


def create_temp_file(data, prefix=''):
    '''Создать буферный файл для отправки пользователю'''
    try:
        # создаем файл вида "prefix-0123456789" в этой же папке как буфер
        filename = './' + prefix + str(int(random.random() * 10**10))
        with open(filename, 'w') as f:
            f.write(data)
            f.close()
        return filename
    except:
        print('Error while running creating temp file')
        traceback.format_exc()
        return False


def remove_temp_file(filename):
    '''Удалить файл (буфер)'''
    try:
        os.remove(filename)
        return True
    except:
        print('Error while removing temp file')
        traceback.format_exc()
        return False
