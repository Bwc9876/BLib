import platform
import subprocess


def ping(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    command = ['ping', param, '1', ip]

    return subprocess.call(command) == 0
