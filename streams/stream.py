from helpers.helpers import *

class Stream:

    def __init__(self, name, substances = None, compositions = None, parameters = None):

        self.name = name
        self.name = name_to_tag(name)

        if substances == None and parameters == None:
            pass
        else:
            self.substances = to_dict(substances)
            self.parameters = to_dict(parameters)
            self.compositions = to_dict(compositions)
            self.substances_names = get_names(substances)
            self.parameters_names = get_names(parameters)