from helpers.helpers import name_to_tag

class Parameter:

    def __init__(self, name, value, units):
        self.name = name
        self.tag = name_to_tag(name)
        self.value = value
        self.units = units