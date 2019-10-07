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

# Uncomment to print inlet, vapor and liquid compositions
#print('Inlet Compositions')
#for tag, comp in inlet.compositions.items():
#    print('{}: {}'.format(tag, comp))
#print('Liquid Compositions')
#for tag, comp in flash.liquid.compositions.items():
#    print('{}: {}'.format(tag, comp))
#print('Vapor Compositions')
#for tag, comp in flash.vapor.compositions.items():
#    print('{}: {}'.format(tag, comp))       