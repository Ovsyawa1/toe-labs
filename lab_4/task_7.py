import matplotlib.pyplot as plt
import numpy as np


def cardioid_polar(a):
    theta = np.linspace(0, 2*np.pi, 1000)
    r = a * np.cos(theta)

    plt.axes(projection='polar')
    plt.plot(theta, r, color='red')
    plt.show()


if __name__ == '__main__':
    cardioid_polar(1)
