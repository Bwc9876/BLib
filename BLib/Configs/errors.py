
class ConfigException(Exception):
    pass


class BadSetup(ConfigException):

    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return self.reason


class ConfigValueError(ConfigException):

    def __init__(self, bad_value):
        self.bad_value = bad_value

    def __str__(self):
        return f"Invalid Value: {self.bad_value} For Config"
