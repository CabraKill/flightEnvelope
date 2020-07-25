import matplotlib.pyplot as plt
from src.classes.makedata import MakeData


class Visualization:
    def __init__(self, makedata: MakeData):
        self.makedata = makedata
        self.fig, self.ax = plt.subplots()
        plt.axis([0, 45, 0, 200])

    def add_plot(self, values_y: [float], values_x: [float], title: str):
        #plt.plot(values_x, values_y, label=title)
        self.ax.plot(values_x, values_y, label=title)

    def set_titles(self, title: str, title_x: str, title_y: str):
        plt.title(title)
        plt.xlabel(title_x)
        plt.ylabel(title_y)

    def add_point(self, x: float, y: float):
        plt.scatter(x, y, s=500)

    def show_envelope(self, alt: float):
        self.add_plot(values_y=self.makedata.td_all(alt),
                      values_x=self.makedata.airplane.velocities, title="td")
        self.add_plot(values_y=self.makedata.tr_all(alt),
                      values_x=self.makedata.airplane.velocities, title="tr")
        self.set_titles(title="Flight Envelope - {} m".format(alt),
                        title_x="velocity", title_y="Trust")
        legend = self.ax.legend(frameon=False, ncol=2)
        plt.show()


def main():
    length = 10
    test = [x for x in range(length)]
    # TODO: Make the class indepent and do finish the main function to work as an example ^^


if __name__ == "__main__":
    main()
