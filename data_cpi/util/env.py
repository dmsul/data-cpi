from os import path
import socket


# Check which machine we're on
HOST = socket.gethostname()
if HOST in ('sullivan-7d', 'sullivan-10d'):
    data_root = "D:\\"
elif HOST in ('DESKTOP-HOME', 'ThinkPad-PC'):
    data_root = "D:\\"
else:
    data_root = r'\\Sullivan-10d'

PROJECT_NAME = 'data-cpi'

DATA_PATH = path.join(data_root, 'Data', PROJECT_NAME)
SRC_PATH = path.join(DATA_PATH, 'src')


def data_path(*args):
    return path.join(DATA_PATH, *args)


def src_path(*args):
    return path.join(SRC_PATH, *args)
