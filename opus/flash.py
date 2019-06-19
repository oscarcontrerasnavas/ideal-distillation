from helpers.helpers import *

class Flash:
    
    def __init__(self, name, inlet, outlets):
        self.name = name
        self.tag = name_to_tag(name)
        self.inlet = to_dict(inlet)
        self.outlets = to_dict(outlets)
        self.inlet_names = get_names(inlet)
        self.outlets_names = get_names(outlets)

