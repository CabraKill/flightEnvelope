from .enviroment import Enviroment
from .airplane import AirPlane


class MakeData:
    # eviroment: env, airplane: airplane, velocity_step: 2
    def __init__(self, eviroment: Enviroment, airplane: AirPlane, velocity_step: 2):
        self.enviroment = eviroment
        self.airplane = airplane
        self.velocity_step = velocity_step

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

    def CD_for_velocity(self, alt: float, velocity: float):
        # CD_for_velocity = CD0+((CL_for_velocity^^(2))*K_for_airplane
        return self.airplane.CD0+((self.CL_for_velocity(alt, velocity)**(2))*self.K_for_airplane())

    def CL_for_velocity(self, alt: float, velocity: float):
        # CL_for_velocity = (2*W)/(density_for_alt*(velocity^^(2))*S)
        return (2*self.airplane.W)/(self.enviroment.density_for_alt(alt)*(velocity**(2))*self.airplane.area)

    def K_for_airplane(self):
        import math
        return 1/(math.pi*self.airplane.aspect_ratio*self.airplane.e0)

    def td(self, alt: float, velocity: float, debug=False):
        if debug:
            print("W: {}\nNh: {}\nPe: {}\nvelocity: {}\ndensity: {}\ndensity_0: {}".format(self.airplane.W,
                                                                                           self.airplane.Nh[velocity], self.airplane.Pe[velocity], velocity, self.enviroment.density_for_alt(alt), self.enviroment.density_for_0))
        return ((self.airplane.Pe[velocity]*self.airplane.Nh[velocity])/velocity)*(self.enviroment.density_for_alt(alt)/self.enviroment.density_for_0)

    def tr(self, alt: float, velocity: float):
        # tr = 0.5*density_for_alt*(velocity^^(2))*S*CD_for_velocity
        return 0.5*self.enviroment.density_for_alt(alt)*(velocity**(2))*self.airplane.area*self.CD_for_velocity(alt, velocity)

    def td_all_old(self, alt: float):
        # td = [self.td(alt, velocity)for velocity in self.airplane.velocities]
        td = []
        for velocity in self.airplane.velocities:
            if velocity > 0:
                td.append(self.td(alt, velocity))
        return td

    def do_all(self, **kwargs):
        value_list = []
        for velocity in self.airplane.velocities:
            if velocity > 0:
                value_list.append(kwargs["func"](
                    alt=kwargs["alt"], velocity=velocity))
        return value_list

    def td_all(self, alt: float):
        return self.do_all(alt=alt, func=self.td)

    def tr_all(self, alt: float):
        return self.do_all(alt=alt, func=self.tr)
