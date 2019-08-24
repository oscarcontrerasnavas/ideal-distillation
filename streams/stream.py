from helpers.helpers import name_to_tag
from helpers.helpers import to_dict
from helpers.helpers import get_names
from streams.parameter import Parameter

class Stream:

    def __init__(self, name,
        substances = None,
        flow_rate = None,
        compositions = None, 
        pressure = None, 
        temperature = None
        ):

        self.name = name
        self.tag = name_to_tag(name)
        self.substances = to_dict(substances)
        self.substances_names = get_names(substances)

        # Flow rates
        if flow_rate == None:
            self.flow_rate = Parameter('Mass Flow Rate', 0, 'kmol/h')
        else:
            self.flow_rate = flow_rate    

        # Compositions
        self.compositions = {}
        if compositions != None:
            for i in range(len(substances)):
                tag = substances[i].tag
                self.compositions[tag] = compositions[i]
        else:
            for tag, _ in self.substances.items():
                self.compositions[tag] = 0        

        # Parameters of the process
        self.pressure = pressure
        self.temperature = temperature 