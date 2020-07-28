from src.functions.intersection import Intersection
from src.model.graph import Graph
from .visualization import Visualization
from src.classes.makedata import MakeData
from src.model.data import Data


class Envelope:
    def __init__(self, makedata: MakeData, data: Data):
        self.makedata = makedata
        self.visualization = None
        self.intersection = Intersection()
        self.data = data

    def add_intersections(self, alt: float, inter: [tuple], debug=False):
        velocities = []
        if debug:
            print("    ", end="")
        for i in inter:
            velocities.append(i[0])
            self.visualization.add_point(x=i[0], y=i[1])
            if debug:
                print(
                    "altitude: {} m - velocity: {} m/s".format(alt, i[0]), end=" ----- ")
        if debug:
            print("")
        if len(velocities) > 0:
            self.data.min_velocity.append(min(velocities))
            self.data.max_velocity.append(max(velocities))
            self.data.output_altitudes.append(alt)

    def find_envelope(self, alt: float, plot=False):
        self.visualization = Visualization(makedata=self.makedata)
        td = self.makedata.td_all(alt)
        tr = self.makedata.tr_all(alt)
        graph = Graph(line1=td, line2=tr,
                      abscissa=self.makedata.airplane.velocities)
        intersections = self.intersection.intersections(
            graph=graph)
        self.add_intersections(alt=alt, inter=intersections, debug=True)
        if plot:
            self.visualization.show_envelope(alt)

    def find_envelope_all(self, start=0, step=500, interations=20, plot=False):
        print("Intersection points:")
        alt = start
        for _ in range(interations):
            self.find_envelope(alt=alt, plot=plot)
            alt += step
