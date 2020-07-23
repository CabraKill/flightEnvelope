class AirPlane:
    def __init__(self, velocities: [float], Nh: [float], Pe: [float], aspect_ratio: float, W: float, area: float, CD0: float):
        self.aspect_ratio = aspect_ratio
        self.W = W
        self.area = area
        self.CD0 = CD0
        self.velocities = velocities
        self.Nh = {}
        for index, Nh_value in enumerate(Nh):
            self.Nh[velocities[index]] = Nh_value
        self.Pe = {}
        for index, Pe_value in enumerate(Pe):
            self.Pe[velocities[index]] = Pe_value

    def to_string(self):
        print("aspect_ratio: {}\nW: {}\narea: {}\nCD0: {}".format(
            self.aspect_ratio, self.W, self.area, self.CD0))
