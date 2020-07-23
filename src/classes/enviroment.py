class Enviroment:
    def __init__(self, sea_alt=0, P0=101.325, T0=288.15, L=0.0065, M=0.0289644, R=8.31447):
        self.g = 9.81
        self.sea_alt = sea_alt
        self.P0 = P0
        self.T0 = T0
        self.L = L
        self.M = M
        self.R = R

        self.density_for_0 = self.density_for_alt(0)

    def pressure_for_alt(self, alt: float):

        return self.P0*((1-((self.L*alt)/(self.T0)))**((self.g*self.M)/(self.R*self.L)))

    def temp_for_alt(self, alt: float):
        return self.T0 - (self.L*alt)

    def density_for_alt(self, alt: float):
        # density_for_alt = ((pressure_for_alt*M)/(R*temp_for_alt))*1000
        return ((self.pressure_for_alt(alt)*self.M)/(self.R*self.temp_for_alt(alt)))*1000
    

