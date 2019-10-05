from helpers.helpers import name_to_tag

class Parameter:
    """Represents a process parameter such as Temperature, Pressure, Volume etc.

    Also, can represent any pair of number-units value.

    Attributes
    ----------
    name : string
        The name of the parameter. I.E.: Temperature.
    tag : string
        The name of the parameter as a return of name_to_tag() function in the
        module helpers.    
    value : float
        The value of the parameter.
    units : string
        In lowercase. The actual units of the measurement.  
    """

    def __init__(self, name, value, units):
        """Create a new Parameter object define as a pair of number-units values
        
        Parameters
        ----------
        name : string
            The name of the parameter. I.E.: Temperature
        value : float
            The value of the parameter
        units : string
            In lowercase. The actual units of the measurement
        """
        self.name = name
        self.tag = name_to_tag(name)
        self.value = value
        self.units = units