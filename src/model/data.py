from src.driver.filedriver import FileDriver

class Data:
    def __init__(self):
        self._reader = FileDriver()
        self.velocities = self._reader.read("src/data/velocities.txt") 
        self.Nh = self._reader.read("src/data/Nh.txt")
        self.Pe = self._reader.read("src/data/Pe.txt")
        self.min_velocity = []
        self.max_velocity = []
