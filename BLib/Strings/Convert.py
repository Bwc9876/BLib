import re
import random


def ListToString(l, sep):
    out = ''
    for i in l:
        if not l.index(i) == 0:
            out += f'{sep}{i}'
        else:
            out += f'{i}'
    return out

def sanitize(in_bytes):
    pattern = "'(.*?)'"
    out = re.search(pattern, str(in_bytes))
    return out.group(1)

def sanitize_double_quotes(in_bytes):
    pattern = '"(.*?)"'
    out = re.search(pattern, str(in_bytes))
    return out.group(1)

def MakeRandomString(possible, length):
    return ''.join(random.choices(possible, k=length))