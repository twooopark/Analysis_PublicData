import numpy as np
import matplotlib.pyplot as plt

def ex1():
    height = [100, 220, 330, 440, 550, 660, 770, 880, 990]
    footsizes = [200, 205, 210, 220, 230, 250, 270, 280, 285]

    fig, subplots = plt.subplots(1, 1)
    subplots.scatter(height,footsizes)
    plt.xlabel('키(Cm)')
    plt.ylabel('발크기(mm)')


    plt.show()

def ex2():
    height = [100, 220, 330, 440, 550, 660, 770, 880, 990]
    temps = [18.5, 17.5, 17, 16.4, 15, 14.3, 13.7, 11.2, 10]

    fig, subplots = plt.subplots(1, 1)
    subplots.scatter(height, temps)
    plt.xlabel('산의 높이(m)')
    plt.ylabel('온도(\'c)')

    plt.show()

def ex3():
    fig, subplots = plt.subplots(1, 1)
    subplots.scatter(
        np.random.random_sample(50),
        np.random.random_integers(0, 100, 50)
    )

    plt.show()


if __name__ == '__main__':
    ex3()