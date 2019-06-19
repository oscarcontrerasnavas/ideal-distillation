from streams.substance import Substance
from streams.stream import Stream
from streams.parameter import Parameter


water = Substance('Water')
methanol = Substance('Methanol')
pressure = Parameter('Pressure', 100, 'bar')
temperature = Parameter('Temperature', 300, 'K')

current = Stream([water, methanol], [pressure, temperature])

print(current.substances_names)
print(current.parameters_names)
print('The Pressure value is {0} {1}'.format(current.parameters['pressure'].value,
current.parameters['pressure'].units))