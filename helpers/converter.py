# -*- coding: utf-8 -*-
"""This module provides functions to convert among different unit sets"""


def temperature(value, from_units, to_units):
    """ Convert among temperature units.

    The options for converting are K, C, F and R. The function is not case
    sensitive.

    Parameters
    ----------
    value : float
        The original value of the temperature.
    from_units : str
        String with the name of the inlet units.
    to_units : str
        String with the desire outlet units.

    Returns
    -------
    float
        The already converted value of the temperature.

     Examples
     --------
     Example of how to convert 80 Celsius Degrees to Fahrenheit

     >>> temperature(80, 'C', 'F')
     176.0

    """

    # Lowering to avoid case sensitive errors
    from_units = from_units.lower()
    to_units = to_units.lower()

    # Check if both units are the same
    if from_units == to_units:
        return value

    # Checking what is the initial units
    # Converting from Celsius
    elif from_units == 'c':
        if to_units == 'f':
            return (value * 9/5) + 32

        elif to_units == 'k':
            return value + 273.15

        elif to_units == 'r':
            return (value * 9/5) + 32 + 459.67

    # Converting from Fahrenheit
    elif from_units == 'f':          
        if to_units == 'c':
            return (value - 32) * 5/9

        elif to_units == 'k':
            return (value - 32) * 5/9 + 273.15

        elif to_units == 'r':
            return value + 459.67

    # Converting from Kelvin
    elif from_units == 'k':        
        if to_units == 'c':
            return value - 273.15

        elif to_units == 'f':
            return (value - 273.15) * 9/5 + 32

        elif to_units == 'r':
            return value * 9/5

    # Converting from Ranking
    elif from_units == 'r':
        if to_units == 'c':
            return (value - 491.67) * 5/9

        elif to_units == 'f':
            return value - 459.67

        elif to_units == 'k':
            return value * 5/9

    return value


def pressure(value, from_units, to_units):
    """ Convert among pressure units.

    The options for converting are kPa, Pa, bar, psi, atm and torr or mmHg. The
    function is not case sensitive.

    Parameters
    ----------
    value : float
        The original value of the pressure.
    from_units : str
        String with the name of the inlet units.
    to_units : str
        String with the desire outlet units.

    Returns
    -------
    float
        The already converted value of the pressure.

     Examples
     --------
     Example of how much is an atm in psi

     >>> pressure(1, 'atm', 'psi')
     14.69

    """

    # Lowering to avoid case sensitive errors
    from_units = from_units.lower()
    to_units = to_units.lower()

    # Check if both units are the same
    if from_units == to_units:
        return value

    # Converting from atmosphere
    elif from_units == 'atm':
        if to_units == 'bar':
            return value * 1.013

        if to_units == 'pa':
            return value * 101325

        if to_units == 'kpa':
            return value * 101.325

        if to_units == 'psi':
            return value * 14.69

        if to_units == 'mmhg' or to_units == 'torr':
            return value * 760 

    # Converting from bar
    elif from_units == 'bar':
        if to_units == 'atm':
            return value * 750.06

        if to_units == 'pa':
            return value * 100000

        if to_units == 'kpa':
            return value * 100

        if to_units == 'psi':
            return value * 14.50

        if to_units == 'mmhg' or to_units == 'torr':
            return value * 750.06 

    # Converting from pascals
    elif from_units == 'pa':
        if to_units == 'atm':
            return value / 101325

        if to_units == 'bar':
            return value / 100000

        if to_units == 'kpa':
            return value / 100

        if to_units == 'psi':
            return value / 6894.75

        if to_units == 'mmhg' or to_units == 'torr':
            return value / 133.322

    # Converting from kilo pascals
    elif from_units == 'kpa':
        if to_units == 'atm':
            return value / 101.325

        if to_units == 'bar':
            return value / 100.000

        if to_units == 'pa':
            return value * 100

        if to_units == 'psi':
            return value / 6.89475

        if to_units == 'mmhg' or to_units == 'torr':
            return value / 0.133322

    # Converting from psi
    if from_units == 'psi':
        if to_units == 'atm':
            return value / 14.69

        if to_units == 'bar':
            return value / 14.15

        if to_units == 'pa':
            return value * 6.89475

        if to_units == 'kpa':
            return value * 6.89e-3

        if to_units == 'mmhg' or to_units == 'torr':
            return value * 51.71                             

    # Converting from Torr or mmhg
    elif to_units == 'mmhg' or to_units == 'torr':
        if to_units == 'atm':
            return value / 760

        if to_units == 'bar':
            return value / 750.062

        if to_units == 'pa':
            return value * 133.322

        if to_units == 'kpa':
            return value * 0.133

        if to_units == 'psi':
            return value / 51.71   

    return value


def time(value, from_units, to_units):
    """ Convert among time units.

    The options for converting are seconds (s), minutes (m), hours, (h) ,
    days (d), months (mon) and years (year, y). The function is not case
    sensitive but some assumptions were made such as:

    * Years have 365 days
    * Months have 30 days

    Parameters
    ----------
    value : float
        The original value of the time.
    from_units : str
        String with the name of the inlet units.
    to_units : str
        String with the desire outlet units.

    Returns
    -------
    float
        The already converted value of the time.

     Examples
     --------
     How many hours does a year have?

     >>> time(1, 'y', 'h')
     14.69

    """

    # Lowering to avoid case sensitive errors
    from_units = from_units.lower()
    to_units = to_units.lower()

    # Check if both units are the same
    if from_units == to_units:
        return value
    
    # Converting from seconds
    elif from_units == 's':
        if to_units == 'm':
            return value / 60

        if to_units == 'h':
            return value / 3600

        if to_units == 'day' or to_units == 'd':
            return value / 86400

        if to_units == 'month' or to_units == 'mon':
            return value / 2592000

        if to_units == 'year' or to_units == 'y':
            return value / 31536000

    # Converting from minutes
    elif from_units == 'm':
        if to_units == 's':
            return value * 60

        if to_units == 'h':
            return value / 60

        if to_units == 'day' or to_units == 'd':
            return value / 1440

        if to_units == 'month' or to_units == 'mon':
            return value / 43200

        if to_units == 'year' or to_units == 'y':
            return value / 525600

    # Converting from hours
    elif from_units == 'h':
        if to_units == 's':
            return value * 3600

        if to_units == 'm':
            return value * 60

        if to_units == 'day' or to_units == 'd':
            return value / 24

        if to_units == 'month' or to_units == 'mon':
            return value / 720

        if to_units == 'year' or to_units == 'y':
            return value / 8760
        
    # Converting from days
    elif from_units == 'day' or from_units == 'd':
        if to_units == 's':
            return value * 86400

        if to_units == 'm':
            return value * 1440

        if to_units == 'h':
            return value * 24

        if to_units == 'month' or to_units == 'mon':
            return value / 30

        if to_units == 'year' or to_units == 'y':
            return value / 365

    # Converting from months
    elif from_units == 'month' or from_units == 'mon':
        if to_units == 's':
            return value * 2592000

        if to_units == 'm':
            return value * 43200

        if to_units == 'h':
            return value * 720

        if to_units == 'day' or to_units == 'd':
            return value * 30

        if to_units == 'year' or to_units == 'y':
            return value / 12

    # Converting from years
    elif from_units == 'year' or from_units == 'y':
        if to_units == 's':
            return value * 31536000

        if to_units == 'm':
            return value * 525600

        if to_units == 'h':
            return value * 8760

        if to_units == 'day' or to_units == 'd':
            return value * 365

        if to_units == 'month' or to_units == 'mon':
            return value * 12                    
    
    return value


def molar_flow(value, from_units, to_units):
    """ Convert among molar flow units.

    The options to convert in and out are kmol, lbmol and mol. This method is a
    helper of a bigger method to convert between molar and mass flow rates.

    Parameters
    ----------
    value : float
        The original value of the molar flow.
    from_units : str
        String with the name of the inlet units.
    to_units : str
        String with the desire outlet units.

    Returns
    -------
    float
        The already converted value of the time.

     Examples
     --------
     Equivalence between mol and kmol

     >>> molar_flow(1000, 'mol', 'kmol')
     1

    """

    # Lowering to avoid case sensitive errors
    from_units = from_units.lower()
    to_units = to_units.lower()

    # Check if both units are the same
    if from_units == to_units:
        return value

    # Converting from mol
    elif from_units == 'mol':
        if to_units == 'lbmol':
            return value / 453.6
        if to_units == 'kmol':
            return value / 1000

    # Converting from lbmol
    elif from_units == 'lbmol':
        if to_units == 'mol':
            return value * 453.6
        if to_units == 'kmol':
            return value * 0.4536

    # Converting from kmol
    elif from_units == 'kmol':
        if to_units == 'mol':
            return value * 1000
        if to_units == 'lbmol':
            return value / 0.4536

    return value


def mass_flow(value, from_units, to_units):
    """ Convert among mass flow units.

    The options to convert in and out are kg, lb and g. This method is a
    helper of a bigger method to convert between molar and mass flow rates.

    Parameters
    ----------
    value : float
        The original value of the mass flow.
    from_units : str
        String with the name of the inlet units.
    to_units : str
        String with the desire outlet units.

    Returns
    -------
    float
        The already converted value of the time.

     Examples
     --------
     Equivalence between g and kg

     >>> mass_flow(1000, 'g', 'kg')
     1

    """

    # Lowering the string to avoid case sensitive errors.
    from_units = from_units.lower()
    to_units = to_units.lower()

    # Check if both units are the same
    if from_units == to_units:
        return value

    # Converting from grams
    elif from_units == 'g' or from_units == 'gr':
        if to_units == 'lb':
            return value / 453.6
        if to_units == 'kg':
            return value / 1000

    # Converting from pounds
    elif from_units == 'lb':
        if to_units == 'g' or to_units == 'gr':
            return value * 453.6
        if to_units == 'kg':
            return value * 0.4536

    # Converting from kilograms
    elif from_units == 'kg':
        if to_units == 'g' or to_units == 'gr':
            return value * 1000
        if to_units == 'lb':
            return value / 0.4536

    return value        


def change_flow_basis(value, substances, compositions, from_units, to_units):
    """Convert between mass and molar flow units.

    The options to convert in and out are the same as molar_flow() and
    mass_flow(). This method is a helper of a bigger method to convert
    between molar and mass flow rates. This function is a helper of the
    bigger method converter.flow_rate()

    Parameters
    ----------
    value : float
        Original value in the inlet set of units
    substances : dict
        Set of Substance.tag : Substance pairs
    compositions : dict
        Set of Substance.tag : composition pairs
    from_units : str
        String with the initial units
    to_units : str
        String with the outlet units

    Returns
    -------
    float
        Value changed to the outlet set of units

    Examples
    --------
    Converting from 1 kmol of a feed that is 30 mol% propane, 10 mol% n-butane,
    15 mol% n-pentane and 45 mol% n-hexane to kg.


    >>> from streams.substance import Substance
    >>> propane = Substance('Propane')
    >>> butane = Substance('Butane')
    >>> pentane = Substance('Pentane')
    >>> hexane = Substance('Hexane')
    >>> substances = {
            'propane' : propane,
            'butane' : butane,
            'pentane' : pentane,
            'hexane' : hexane
        }
    >>> compositions = {
            'propane' : 0.3,
            'butane' : 0.1,
            'pentane' : 0.15,
            'hexane' : 0.45
        }
    >>> change_flow_basis(1, substances, compositions, 'kmol', 'kg')
    68.64

    """

    # Lowering the string to avoid case sensitive errors.
    from_units = from_units.lower()
    to_units = to_units.lower()

    # Converting from molar to mass flow
    if (from_units == 'kmol' or from_units == 'lbmol' or from_units == 'mol')\
            and (to_units == 'kg' or to_units == 'lb' or to_units ==
                 'g' or to_units == 'gr'):

        weight = 0
        for tag, substance in substances.items():
            weight += compositions[tag] * substance.molecular_weight

        total = value * weight
        
        # Checking the new from_units
        if from_units == 'kmol':
            from_units = 'kg'
        elif from_units == 'lbmol':
            from_units = 'lb'
        elif from_units == 'mol':
            from_units = 'g'

        return mass_flow(total, from_units, to_units)

    # Converting from mass to molar flow
    elif (from_units == 'kg' or from_units == 'lb' or from_units == 'g' or
            from_units == 'gr') and (to_units == 'kmol' or to_units ==
                                     'lbmol' or to_units == 'mol'):

        weight = 0
        for tag, substance in substances.items():
            weight += compositions[tag] / substance.molecular_weight

        total = value * weight
        
        # Checking the new from_units
        if from_units == 'kg':
            from_units = 'kmol'
        elif from_units == 'lb':
            from_units = 'lbmol'
        elif from_units == 'g' or from_units == 'gr':
            from_units = 'mol'

        return molar_flow(total, from_units, to_units)

    else:
        return value

    
def flow_rate(value, substances, compositions, from_units, to_units):
    """Converting flow rates.

    The options available in this functions are listed below:

    * Flow: kmol, lbmol, mol, kg, lb, g or gr
    * Time: seconds (s), minutes (m), hours (h) ,days (d), months (mon) and
    years (year, y).

    Parameters
    ----------
    value : float
        Original value in the inlet set of units
    substances : dict
        Set of Substance.tag : Substance pairs
    compositions : dict
        Set of Substance.tag : composition pairs
    from_units : str
        String with the initial units
    to_units : str
        String with the outlet units

    Returns
    -------
    float
        Value changed to the outlet set of units

    Examples
    --------
    Converting from 1 kmol/h of a feed that is 30 mol% propane, 10 mol%
    n-butane, 15 mol% n-pentane and 45 mol% n-hexane to g/s.

    >>> from streams.substance import Substance
    >>> propane = Substance('Propane')
    >>> butane = Substance('Butane')
    >>> pentane = Substance('Pentane')
    >>> hexane = Substance('Hexane')
    >>> substances = {
            'propane' : propane,
            'butane' : butane,
            'pentane' : pentane,
            'hexane' : hexane
        }
    >>> compositions = {
            'propane' : 0.3,
            'butane' : 0.1,
            'pentane' : 0.15,
            'hexane' : 0.45
        }
    >>> flow_rate(1, substances, compositions, 'kmol/h', 'g/s')
    68.64
    """

    # Lowering the string to avoid case sensitive errors.
    from_units = from_units.lower()
    to_units = to_units.lower()

    # The first part of the split string will be the flow units and the
    # second part is the time units.
    from_units = from_units.split('/')
    to_units = to_units.split('/')
    time_value = time(1, from_units[1], to_units[1])

    # Don't need time units more
    from_units = from_units[0]
    to_units = to_units[0]

    # Check the sort of conversion. From Mass to Mass, From Molar to Molar or
    # Change of basis
    # Converting from molar to molar flows
    if (from_units == 'kmol' or from_units == 'lbmol' or from_units == 'mol')\
            and (to_units == 'kmol' or to_units == 'lbmol' or to_units ==
                 'mol'):
        flow_value = molar_flow(value, from_units, to_units)

    # Converting from mass to mass flows
    elif (from_units == 'kg' or from_units == 'lb' or from_units == 'g'
          or from_units == 'gr') and (to_units == 'kg' or to_units == 'lb' or
                                      to_units == 'g' or to_units == 'gr'):

        flow_value = mass_flow(value, from_units, to_units)

    else:
        flow_value = change_flow_basis(value, substances, compositions,
                                       from_units, to_units)

    return flow_value / time_value
