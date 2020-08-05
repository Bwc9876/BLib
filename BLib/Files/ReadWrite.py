import os
import shutil
from zipfile import ZipFile

def DeleteIfExists(file):
    if os.path.exists(file):
        if os.path.isfile(file):
            os.remove(file)
        else:
            shutil.rmtree(file)

def GetLinesAsList(file, include_newlines=False):
    if os.path.exists(file):
        if os.path.isfile(file):
            f = open(file, 'r')
            lines= []
            for line in f.readlines():
                if not include_newlines:
                    lines += [line.strip()]
                else:
                    lines += [line]
            return lines
        else:
            raise FileNotFoundError(f"'{file}' is a directory")
    else:
        raise FileNotFoundError(f"file '{file}' doesn't exist")

def Zip(name):
    with ZipFile(f'{name}.zip', 'w') as zipObj:
        for folder_name, sub_folders, file_names in os.walk('Data'):
            for filename in file_names:
                file_path = os.path.join(folder_name, filename)
                zipObj.write(file_path)
        zipObj.close()

def Unzip(name):
    with ZipFile(f'{name}.zip', 'r') as zipObj:
        zipObj.extractall()

