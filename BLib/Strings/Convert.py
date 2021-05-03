import random
import re


def list_to_sentence(source_list):
    result = ""
    for item in source_list:
        if source_list[-1] == item:
            if len(source_list) == 1:
                result += item + "."
            else:
                result += "and " + item + "."
        else:
            if len(source_list) == 2:
                result += item + " "
            else:
                result += item + ", "
    return result


def sanitize(in_bytes):
    pattern = "'(.*?)'"
    out = re.search(pattern, str(in_bytes))
    return out.group(1)


def sanitize_double_quotes(in_bytes):
    pattern = '"(.*?)"'
    out = re.search(pattern, str(in_bytes))
    return out.group(1)


def make_random_string(possible, length):
    return ''.join(random.choices(possible, k=length))
