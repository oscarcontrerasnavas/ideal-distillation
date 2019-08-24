from helpers.helpers import name_to_tag
from helpers import converter
from scipy.optimize import newton

class Flash:
    
    def __init__(self, name, inlet, vapor, liquid):
        self.name = name
        self.tag = name_to_tag(name)
        self.inlet = inlet
        self.vapor = vapor
        self.liquid = liquid

    def solve(self):
        if self.inlet.pressure != None and \
            self.inlet.temperature != None and \
            self.vapor.pressure == None and \
            self.liquid.temperature == None:
            
            # r = v/f
            def rachford_rice(r): 
                sum = 0.0
                for tag, substance in self.inlet.substances.items():
                    Zi = self.inlet.compositions[tag]
                    Ps = substance.get_vapor_pressure(self.inlet.temperature)
                    Ps = converter.pressure(Ps, 'bar', 'kpa')
                    Ki = Ps/self.inlet.pressure.value
                    sum = sum + (Zi*(Ki-1)) / (1 + r*(Ki-1))
                return sum

            # solving r
            r = newton(rachford_rice, 0.5)

            # Solving flow rates for vapor
            self.vapor.flow_rate.name = self.inlet.flow_rate.name
            self.vapor.flow_rate.value = r * self.inlet.flow_rate.value
            self.vapor.flow_rate.units = self.inlet.flow_rate.units

            # Solving flow rates for liquid
            self.liquid.flow_rate.name = self.inlet.flow_rate.name
            self.liquid.flow_rate.value = self.inlet.flow_rate.value \
                                            - self.vapor.flow_rate.value
            self.liquid.flow_rate.units = self.inlet.flow_rate.units

            # solving yi
            for tag, substance in self.inlet.substances.items():
                Zi = self.inlet.compositions[tag]
                Ps = substance.get_vapor_pressure(self.inlet.temperature)
                Ps = converter.pressure(Ps, 'bar', 'kpa')
                Ki = Ps/self.inlet.pressure.value
                self.vapor.compositions[tag] = Ki*Zi/(1 + (Ki-1)*r)

            # solving xi
            for tag, substance in self.inlet.substances.items():
                Zi = self.inlet.compositions[tag]
                Ps = substance.get_vapor_pressure(self.inlet.temperature)
                Ps = converter.pressure(Ps, 'bar', 'kpa')
                Ki = Ps/self.inlet.pressure.value
                self.liquid.compositions[tag] = Zi/(1 + (Ki-1)*r)    

