from .enviroment import Enviroment
from .airplane import AirPlane
from src.driver.visualization import Visualization


class PlotData:
    # eviroment: env, airplane: airplane, velocity_step: 2
    def __init__(self, eviroment: Enviroment, airplane: AirPlane, velocity_step: 2):
        self.enviroment = eviroment
        self.airplane = airplane
        self.velocity_step = velocity_step
        self.visual = Visualization()

    def plot(self, alt: float):
        self.visual.plot(values_x=self.get_td_all(alt), values_y=[
                         x * 2 for x in range(1, len(self.get_td_all(alt))+1)], title="Tr")

    """
    td = ((Pe(w)*Nh(%))/velocity)*(density_for_alt/density_for_0)

    tr = 0.5*density_for_alt*(velocity^^(2))*S*CD_for_velocity

    CD_for_velocity = CD0+((CL_for_velocity^^(2))*K_for_airplane

    CL_for_velocity = (2*W)/(density_for_alt*(velocity^^(2))*S)

    K_for_airplane = 1/(math.Pi()*AR*e0)

    density_for_alt = ((pressure_for_alt*M)/(R*temp_for_alt))*1000

    pressure_for_alt = P0*((1-((L*alt)/(T0)))^((g*M)/(R*L)))

    temp_for_alt = T0 - (L*alt)
    """

    def get_td(self, alt: float, velocity: float, debug=False):
        if debug:
            print("W: {}\nNh: {}\nPe: {}\nvelocity: {}\ndensity: {}\ndensity_0: {}".format(self.airplane.W,
                                                                                           self.airplane.Nh[velocity], self.airplane.Pe[velocity], velocity, self.enviroment.density_for_alt(alt), self.enviroment.density_for_0))
        return ((self.airplane.Pe[velocity]*self.airplane.Nh[velocity])/velocity)*(self.enviroment.density_for_alt(alt)/self.enviroment.density_for_0)

    def get_tr(self):
        return 1

    def get_CD_for_velocity(self):
        return 1

    def get_CL_for_velocity(self):
        return 1

    def get_K_for_airplane(self):
        return 1

    def get_td_all(self, alt: float):
        # td = [self.get_td(alt, velocity)for velocity in self.airplane.velocities]
        td = []
        for velocity in self.airplane.velocities:
            if velocity > 0:
                td.append(self.get_td(alt, velocity))
        return td
