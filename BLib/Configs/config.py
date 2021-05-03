from BLib.Files.Classes import save_object_to_file, get_obj_from_file
from BLib.Configs.errors import *


class Data:
    def __init__(self, data=None, **kargs):
        if data is None:
            for key, val in kargs.items():
                self.__dict__[key] = val
        else:
            self.__dict__ = data


class Configuration:

    def __init__(self, filename="config", auto_save=False, initial=None):
        if initial is None:
            initial = {}
        self._filename = filename
        self._data = Data(data=initial)
        self.auto_save = auto_save

    def save(self):
        save_object_to_file(self._data, filename=self._filename, replace=True)

    def load(self):
        self._data = get_obj_from_file(self._data, self._filename)

    def get_value(self, value_name, default=None):
        return self._data.__dict__.get(value_name, default)

    def set_value(self, value_name, new_value):
        self._data.__dict__[value_name] = new_value
        if self.auto_save:
            self.save()

    def value_exists(self, value_name):
        try:
            x = self._data.__dict__[value_name]
            return True
        except KeyError:
            return False

    def as_dict(self):
        return self._data.__dict__.copy()

    def from_dict(self, new_data):
        self._data.__dict__ = new_data
        if self.auto_save:
            self.save()


