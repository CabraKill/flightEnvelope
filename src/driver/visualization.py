import matplotlib.pyplot as plt


class Visualization:
    def __init__(self):
        pass

    def plot(self, values_x: [float], values_y: [float], title: str):
        print(values_y)
        plt.plot(values_x, values_y)
        plt.ylabel(title)
        plt.show()
