import os

def GetFilesInDirByExt(dir, ext):

    out = []

    if not os.path.exists(dir):
        raise FileNotFoundError(f"'{dir}' not found")
    if os.path.isfile(dir):
        raise FileNotFoundError(f"'{dir}' is a file")

    for f in os.listdir(dir):
        if f.endswith(f".{ext}"):
            out += [os.path.join(dir, f)]

    return out

def GetFilesInDir(dir):
    out = []

    if not os.path.exists(dir):
        raise FileNotFoundError(f"'{dir}' not found")
    if os.path.isfile(dir):
        raise FileNotFoundError(f"'{dir}' is a file")

    for f in os.listdir(dir):
        out += [os.path.join(dir, f)]

    return out
