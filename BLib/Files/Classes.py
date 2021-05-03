import json
import os


def object_to_json(obj):
    return json.dumps(obj.__dict__)


def json_to_obj(obj, data):
    obj.__dict__ = json.loads(data)
    return obj


def json_to_new_obj(source_class, data):
    obj = source_class().__dict__ = json.loads(data)
    return obj


def save_object_to_file(obj, filename=None, replace=False):
    if filename is None:
        filename = f"{obj.__class__.__name__}.json"

    json_str = object_to_json(obj)

    if os.path.exists(f"{filename}.json") and replace:
        os.remove(f"{filename}.json")
    elif os.path.exists(f"{filename}.json") and not replace:
        raise FileExistsError(
            f"The file '{filename}.json' already exists, set replace=True if you're okay with replacing the file")

    f = open(f"{filename}.json", "w+")

    f.write(json_str)

    f.close()

    return os.path.abspath(f"{filename}.json")


def get_obj_from_file(cl, filename):
    if not os.path.exists(f"{filename}.json"):
        raise FileNotFoundError(f"file '{filename}.json' not found")

    f = open(f"{filename}.json", 'r')

    json_str = f.read()

    new_obj = json_to_obj(cl, json_str)

    return new_obj
