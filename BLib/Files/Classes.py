import json
import os

def ClasstoJson(cl):
    return json.dumps(cl.__dict__)

def JsontoClass(cl, data):
    cl.__dict__ = json.loads(data)
    return cl

def SaveClassToFile(cl, filename="PythonClass", replace=False):
    jsonstr = ClasstoJson(cl)

    if os.path.exists(f"{filename}.json") and replace:
        os.remove(f"{filename}.json")
    elif os.path.exists(f"{filename}.json") and not replace:
        raise FileExistsError(f"The file '{filename}.json' already exists, set replace=True if you're okay with replacing the file")

    f = open(f"{filename}.json", "w+")

    f.write(jsonstr)

    f.close()

    return os.path.abspath(f"{filename}.json")

def GetClassFromFile(cl, filename):
    if not os.path.exists(f"{filename}.json"):
        raise FileNotFoundError(f"file '{filename}.json' not found")

    f = open(f"{filename}.json", 'r')

    jsonstr = f.read()

    newcl = JsontoClass(cl, jsonstr)

    return newcl

