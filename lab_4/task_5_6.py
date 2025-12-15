from scipy.integrate import tplquad
import math as m


def integral():
    area = tplquad(lambda x, y, z: x**y - z, 0, 1, 0, 1, 0, 1)
    print(f"{area[0]:.7f}")

    return area


def count_sub():
    result = m.log(2) - 1 / 2
    print(f"{result:.7f}")

    return result


if __name__ == '__main__':
    ans_1 = integral()
    ans_2 = count_sub()
