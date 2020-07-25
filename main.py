from dependencies import *


def main():
    filedriver = FileDriver()
    data = Data()
    enviroment = Enviroment()
    airplane = AirPlane(
        #velocities=[velocity*2 for velocity in range(1, 21)],
        #Nh=[0.086767, 0.17147, 0.25282, 0.32988, 0.40197, 0.46852, 0.52904, 0.58303, 0.62991,0.66894, 0.69904, 0.71862, 0.72522, 0.71483, 0.68056, 0.60971, 0.47616, 0.21686, 0, 0],
        #Pe=[734.82, 733.93, 731.74, 727.75, 721.48, 712.5, 700.37, 684.68, 665.03,641.03, 612.3, 578.46, 539.14, 493.99, 442.63, 384.73, 319.93, 247.9, 168.29, 80.765],
        velocities=[float(x) for x in data.velocities],
        Nh=[float(x) for x in data.Nh],
        Pe=[float(x) for x in data.Pe],
        aspect_ratio=7, W=176.58, area=1.512, CD0=0.002, e0=0.7389)

    makedata = MakeData(airplane=airplane,
                        eviroment=enviroment, velocity_step=2)

    visual = Visualization(makedata)

    envelope = Envelope(makedata=makedata, visualization=visual, data=data)

    #envelope.find_envelope_all(plot=True)
    envelope.find_envelope(alt=600, plot=True)

    #filedriver.write("src/data/minvelocities.txt", data.min_velocity)
    #filedriver.write("src/data/maxvelocities.txt", data.max_velocity)


if __name__ == "__main__":
    main()
