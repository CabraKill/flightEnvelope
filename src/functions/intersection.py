from src.model.graph import Graph


class Intersection:
    def __init__(self):
        pass

    """
    td = ((Pe(w)*Nh(%))/velocity)*(density_for_alt/density_for_0)

    tr = 0.5*density_for_alt*(velocity^^(2))*S*CD_for_velocity
    """

    def intersections(self, graph: Graph, debug=False):
        intersection_values = []
        state = None  # True for above, False for bellow
        for index, x in enumerate(graph.abscissa):
            if state == None:
                if graph.line1[index] > graph.line2[index]:
                    state = True
                else:
                    state = False
                    continue
            if graph.line1[index] > graph.line2[index] and state == True:
                continue
            if graph.line1[index] < graph.line2[index] and state == False:
                continue
            state = not state
            intersection_values.append(
                ((graph.abscissa[index-1], graph.line1[index-1]), (x, graph.line1[index])))

        if debug:
            print("Intersections: {}".format(intersection_values))
        interpolated_intersection = []
        for i in intersection_values:
            interpolated_intersection.append(self.interpolate(i[0], i[1]))
        return interpolated_intersection

    def min_insetersection(self, graph1: Graph):
        pass

    def max_insetersection(self, graph1: Graph, graph2: Graph):
        pass

    def interpolate(self, point1: tuple, point2: tuple):
        return (abs(point1[0]-point2[0])/2 + min(point1[0], point2[0]), abs(point1[1]-point2[1])/2 + min(point1[1], point2[1]))
