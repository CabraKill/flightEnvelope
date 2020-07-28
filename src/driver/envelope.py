from src.functions.intersection import Intersection
from src.model.graph import Graph
from src.classes.makedata import MakeData
from src.model.data import Data
from src.driver.visualization import Visualization
from src.functions.linearization_graph import LinearizationGraph


class Envelope:
    def __init__(self, makedata: MakeData, data: Data):
        self.makedata = makedata
        self.visualization = None
        self.intersection = Intersection()
        self.data = data

    def add_intersections(self, line: int, alt: float, inter: [tuple], debug=False):
        velocities = []
        if debug and len(inter) > 0:
            print("    ", end="")
        for i in inter:
            velocities.append(i[0])
            self.visualization.add_point(x=i[0], y=i[1])
            if debug:
                print(
                    "line: {} - altitude: {} m - velocity: {} m/s".format(line, alt, i[0]), end=" ----- ")
        if debug and len(inter) > 0:
            print("")
        if len(velocities) > 0:
            self.data.min_velocity.append(min(velocities))
            self.data.max_velocity.append(max(velocities))
            self.data.output_altitudes.append(alt)

    def find_envelope(self, line: int, alt: float, plot=False):
        self.visualization = Visualization(makedata=self.makedata)
        td = self.makedata.td_all(alt)
        tr = self.makedata.tr_all(alt)
        graph = Graph(line1=td, line2=tr,
                      abscissa=self.makedata.airplane.velocities)
        intersections = self.intersection.intersections(
            graph=graph)
        self.add_intersections(
            line=line, alt=alt, inter=intersections, debug=True)
        if plot:
            self.visualization.show_envelope(alt)

    def find_envelope_all(self, start=0, step=500, interations=20, plot=False):
        print("Intersection points:")
        alt = start
        for i in range(interations):
            self.find_envelope(line=i, alt=alt, plot=plot)
            alt += step
        self.data.min_velocity_linearized = LinearizationGraph(
        ).linearization(values=self.data.min_velocity)
        self.data.max_velocity_linearized = LinearizationGraph(
        ).linearization(values=self.data.max_velocity)
