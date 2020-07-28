from src.driver.filedriver import FileDriver


class Data:
    def __init__(self):
        self._fileDriver = FileDriver()
        self.velocities = self._fileDriver.read("src/data/velocities.txt")
        self.Nh = self._fileDriver.read("src/data/Nh.txt")
        self.Pe = self._fileDriver.read("src/data/Pe.txt")
        self.min_velocity = []
        self.min_velocity_linearized = []
        self.max_velocity = []
        self.max_velocity_linearized = []
        self.output_altitudes = []

    def save(self):
        self._fileDriver.write(
            "src/data/min_velocities.txt", self.min_velocity)
        self._fileDriver.write(
            "src/data/min_velocities_linearized.txt", self.min_velocity_linearized)
        self._fileDriver.write(
            "src/data/max_velocities.txt", self.max_velocity)
        self._fileDriver.write(
            "src/data/max_velocities_linearized.txt", self.max_velocity_linearized)
        self._fileDriver.write(
            "src/data/output_altitudes.txt", self.output_altitudes)
