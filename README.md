# Simple Flash Tank (Distillation)

The present repository scrap data from the [NIST
Webbook](https://webbook.nist.gov/) for Antoine constants
and use them for calculating the vapor pressure and **K-values** for each of the
components in a multicomponent stream line. An example file is included within
and shows the general steps to solve a flash (and ideal) distillation problem.

The mathematical background is explained in my
[blog](https://oscarcontrerasnavas.github.io/ideal-multicomponent-solver-and-maths/)
and below this line a brief description of the modules.

## Parameter, Substance and Stream objects

Trying to use the OOP the repository are made of Classes that represent real
concepts in real life.

1. Parameter: Represents process parameters as temperature, pressure and all
   measurements that need units to be full described 

2. Substance: Represents real substances like water, propanol etc... Some of the
   methods allows user to obtain certain physical and chemical properties.

3. Stream: Represents stream lines, includes parameter of the stream and the
   substances transported.

## External Libraries

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Numpy/Scipy](https://www.scipy.org/)

## main.py File

``` Python
from streams.substance import Substance
from streams.stream import Stream
from streams.parameter import Parameter
from opus.flash import Flash


"""
A flash chamber operating at 50°C and 200 kPa is separating 1000 kmol/h of a
feed that is 30 mol% propane, 10 mol% n-butane, 15 mol% n-pentane and 45 mol%
n-hexane. Find the product compositions and flow rates
"""

# Define substances
propane = Substance('Propane')
butane = Substance('Butane')
pentane = Substance('Pentane')
hexane = Substance('Hexane')
substances = [propane, butane, pentane, hexane]
composition = [0.3, 0.1, 0.15, 0.45]

# Define Parameters
temperature = Parameter('Temperature', 323, 'K')
pressure = Parameter('Pressure', 200, 'kPa')
flow_rate = Parameter('Mass Flow Rate', 1000,'kmol/h')

#Define Streams
inlet = Stream('Inlet', substances, flow_rate, composition, pressure, temperature)
vapor = Stream('Vapor', substances)
liquid = Stream('Liquid', substances)

# Define a Flash
flash = Flash('V-101', inlet, vapor, liquid)
flash.solve()
vapor = flash.vapor
liquid = flash.liquid
```

### Results

|Feed              |Vapor              |Liquid             |
|------------------|-------------------|-------------------|
|*F* = 1000 kmol/h |*V* = 503.8 kmol/h |*L* = 496.2 kmol/h |
|*z_propane* = 0.3 |*y_propane* = 0.534|*x_propane* = 0.062|
|*z_butane* = 0.1  |*y_butane* = 0.142 |*x_butane* = 0.058 |
|*z_pentane* = 0.15|*y_pentane* = 0.133|*x_pentane* = 0.168|
|*z_hexane* = 0.45 |*y_hexane* = 0.191 |*x_hexane* = 0.713 |

## More examples

There is a Jupyter Notebook renderer with two additional examples. You are able
of read it
[here](https://nbviewer.jupyter.org/github/oscarcontrerasnavas/ideal-distillation-solver/blob/master/examples.ipynb)


## Mathematical Background

[Post in my blog](https://oscarcontrerasnavas.github.io/ideal-multicomponent-solver-and-maths/)