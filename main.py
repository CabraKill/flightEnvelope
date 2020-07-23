from dependencies import *


def main():
    enviroment = Enviroment()
    airplane = AirPlane(velocities=[
        velocity*2 for velocity in range(0,21)],
        Nh=[0, 0.086767, 0.17147, 0.25282, 0.32988, 0.40197, 0.46852, 0.52904, 0.58303, 0.62991,
            0.66894, 0.69904, 0.71862, 0.72522, 0.71483, 0.68056, 0.60971, 0.47616, 0.21686,0,0],
        Pe=[734.97, 734.82, 733.93, 731.74, 727.75, 721.48, 712.5, 700.37, 684.68, 665.03,
            641.03, 612.3, 578.46, 539.14, 493.99, 442.63, 384.73, 319.93, 247.9, 168.29, 80.765],
        aspect_ratio=7, W=176.58, area=1.512, CD0=0.002)

    plotdata = PlotData(airplane=airplane,
                        eviroment=enviroment, velocity_step=2)
    print(plotdata.get_td(500, 2))
    plotdata.plot(500)
    # plotdata.plot()


if __name__ == "__main__":
    main()
