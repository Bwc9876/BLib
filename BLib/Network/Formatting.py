def RemoveNullTerminator(string):
    if '\\x00' in string:
        return string.replace('\\x00', '')
    else:
        return string