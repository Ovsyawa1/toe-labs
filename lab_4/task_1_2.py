import numpy as np


def main():
    matrix = np.random.randint(
        low=-100,
        high=100,
        size=[3, 3]
    )
    print(
        "Исходная матрица:\n"
        f"{matrix}"
    )
    print(
        "\nИнвертированная матрица:\n"
        f"{np.linalg.inv(matrix)}"
    )

    # Вектор
    n = 5
    vector = 1 - np.random.rand(n)
    print(f"\nВектор: {np.round(vector, 3)}")


if __name__ == '__main__':
    main()
