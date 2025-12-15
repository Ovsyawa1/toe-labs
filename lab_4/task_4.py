import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from copy import copy


def main():
    X0 = 2
    Y0 = 2

    X, Y = np.meshgrid(np.arange(-4, 4, 0.2), np.arange(-4, 4, 0.2))
    circle_patch_1 = Circle((-X0, -Y0), 0.2)
    circle_patch_2 = Circle((X0, Y0), 0.2)

    Ex = ((X + X0) / ((X + X0)**2 + (Y + Y0)**2) -
        (X - X0) / ((X - X0)**2 + (Y - Y0)**2))

    Ey = ((Y + Y0) / ((X + X0)**2 + (Y + Y0)**2) -
        (Y - Y0) / ((X - X0)**2 + (Y - Y0)**2))

    plt.figure(figsize=(6, 6))
    plt.streamplot(X, Y, Ex, Ey, color="black")
    plt.title('График потоков')
    plt.gca().add_patch(copy(circle_patch_1))
    plt.gca().add_patch(copy(circle_patch_2))
    plt.show()

    plt.figure(figsize=(6, 6))
    plt.quiver(X, Y, Ex, Ey, scale=50)
    plt.title('quiver')
    plt.gca().add_patch(copy(circle_patch_1))
    plt.gca().add_patch(copy(circle_patch_2))
    plt.show()


if __name__ == '__main__':
    main()
