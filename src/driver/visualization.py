import matplotlib.pyplot as plt
from src.classes.makedata import MakeData


class Visualization:
    def __init__(self, makedata: MakeData):
        self.makedata = makedata
        plt.axis([0, 45, 0, 200])

    def add_plot(self, values_y: [float], values_x: [float]):
        plt.plot(values_x, values_y)

    def set_title_y(self, title: str):
        plt.ylabel(title)
    
    def add_point(self,x: float,y:float):
        plt.scatter(x, y, s=500)

    def show_at(self, alt: float):
        self.add_plot(values_y=self.makedata.td_all(alt),
                      values_x=self.makedata.airplane.velocities)
        self.add_plot(values_y=self.makedata.tr_all(alt),
                      values_x=self.makedata.airplane.velocities)
        self.set_title_y(title="Tr")
        plt.show()

