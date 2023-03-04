import os
import random
import traceback

def linux_command_ex(command):
    try:
        stream = os.popen(f'{command}')
        res = stream.read()
        return res
    except:
        print('Error while running linux command')
        traceback.format_exc()
        return False


def create_temp_file(data, prefix=''):
    try:
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
    try:
        os.remove(filename)
        return True
    except:
        print('Error while removing temp file')
        traceback.format_exc()
        return False