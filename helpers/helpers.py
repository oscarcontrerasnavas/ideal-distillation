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
    my_list = []
    for item in items:
        my_list.append(item)
    return my_list    


def get_names(items):
    names = []
    for item in items:
        names.append(item.name)
    return names


def name_to_tag(name):
    return name.lower().replace(' ', '+')
