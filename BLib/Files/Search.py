import os


def get_files_in_dir_by_extension(directory, ext):
    out = []

    if not os.path.exists(directory):
        raise FileNotFoundError(f"'{directory}' not found")
    if os.path.isfile(directory):
        raise FileNotFoundError(f"'{directory}' is a file")

    for f in os.listdir(directory):
        if f.endswith(f".{ext}"):
            out += [os.path.join(directory, f)]

    return out


def get_all_files_in_dir(directory):
    out = []

    if not os.path.exists(directory):
        raise FileNotFoundError(f"'{directory}' not found")
    if os.path.isfile(directory):
        raise FileNotFoundError(f"'{directory}' is a file")

    for f in os.listdir(directory):
        out += [os.path.join(directory, f)]

    return out
