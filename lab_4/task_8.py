import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, filtfilt


def main():
    point_size = 500
    x_axis = np.linspace(0, 120, point_size)
    y_axis = np.sin(x_axis / 60 * 2 * np.pi)

    y_axis_noise = y_axis + np.random.uniform(-1, 1, point_size) * 0.2

    # Фильтрация сигнала
    fs = (point_size - 1) / 120
    cutoff = 0.15
    b, a = butter(4, cutoff, btype="low", fs=fs)
    y_smooth = filtfilt(b, a, y_axis_noise)

    # Графики
    plt.subplot(1, 2, 1)
    plt.plot(x_axis, y_axis, label='Без шума')
    plt.plot(x_axis, y_axis_noise, label='Шум')
    plt.grid(True)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(x_axis, y_axis, label='Без шума')
    plt.plot(x_axis, y_smooth, label='Фильтр Баттера')
    plt.grid(True)
    plt.legend()

    plt.show()


if __name__ == '__main__':
    main()
