import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth


def main():
    # Стартовые условия
    fs = 1000
    T = 6
    f = 0.5

    time_axis = np.linspace(0, T, fs)
    triangle_neg = sawtooth(2 * np.pi * f * time_axis, width=0.5)
    triangle = (triangle_neg + 1) / 2
    saw_neg = sawtooth(2 * np.pi * f * time_axis)
    saw = (saw_neg + 1) / 2

    plt.subplot(1, 2, 1)
    plt.axhline(y=0, color='black', linestyle='-')
    plt.plot(time_axis, triangle, label="Triangle", color='red')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(time_axis, saw, label="Saw", color='blue')
    plt.axhline(y=0, color='black', linestyle='-')
    plt.grid(True)

    plt.xlabel("t")
    plt.ylabel("f(t)")
    plt.show()


if __name__ == '__main__':
    main()
