"""
    This module list some simple functions that does not belong to any other
    module.
"""


def to_dict(items):
    """ Transform a list of Objects into a dictionary using their tag as key

    Parameters
    ----------
    items : list
        List of Substances or Streams Objects, also any kind of object with
        attribute Object.tag

    Returns
    -------
    dict
        It returns a dictionary in which key, value pairs are Object.tag and
        Object respectively.

    Examples
    --------
    List of Substance Objects to dictionary

    >>> from streams.substance import Substance
    >>> propane = Substance('Propane')
    >>> pentane = Substance('Pentane')
    >>> substances = [propane, pentane]
    >>> to_dict(substances)
    {'pentane': <streams.substance.Substance>,
    'propane': <streams.substance.Substance>}

    """
    dictionary = {}
    for item in items:
        dictionary[item.tag] = item
    return dictionary


def to_list(items):
    """Helper to parse items by argument as a list of items
    
    Parameters
    ----------
    items : object
        The items argument could be an arbitrary number of objects Substance or
        Stream
    
    Returns
    -------
    list
        A list of items. Accessible by index.
    """
    my_list = []
    for item in items:
        my_list.append(item)
    return my_list    


def get_names(items):
    """Obtain the name from objects with the object.name property and store 
    them in a list.
    
    Parameters
    ----------
    items : object
        Parameter, Substance or Stream objects with object.name property
    
    Returns
    -------
    list
        List of names
    """
    names = []
    for item in items:
        names.append(item.name)
    return names


def name_to_tag(name):
    """Remove spaces from names with more than one word and separated with '+'.
    Ready for using them as part of the link for scraping.
    
    Parameters
    ----------
    name : string
        Name of the substance
    
    Returns
    -------
    string
        Name of the substance without spaces and in lowercase.
    """
    return name.lower().replace(' ', '+')
