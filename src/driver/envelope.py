from src.functions.intersection import Intersection
from src.model.graph import Graph
from .visualization import Visualization
from src.classes.makedata import MakeData


class Envelope:
    def __init__(self, makedata: MakeData, visualization: Visualization):
        self.makedata = makedata
        self.visualization = visualization
        self.intersection = Intersection()

    def add_intersections(self, alt: float, inter: [tuple], debug=False):

        for i in inter:
            self.visualization.add_point(x=i[0], y=i[1])
            if debug:
                print(
                    "altitude: {} m - velocity: {} m/s".format(alt, i[0]), end=" ----- ")
        if debug:
            print("")

    def find_envelope(self, alt: float):
        td = self.makedata.td_all(alt)
        tr = self.makedata.tr_all(alt)
        graph = Graph(line1=td, line2=tr,
                      abscissa=self.makedata.airplane.velocities)
        intersections = self.intersection.intersections(
            graph=graph)
        self.add_intersections(alt=alt, inter=intersections, debug=True)
        #self.visualization.show_at(alt)

    def find_envelope_all(self, start=0, step=500, interations=20):
        print("Intersections point:\n\t", end="")
        alt = start
        for _ in range(interations):
            self.find_envelope(alt=alt)
            alt += step
