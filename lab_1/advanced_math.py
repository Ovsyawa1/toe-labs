from math import factorial, log, sin, cos, sqrt, tan, radians
from decorators import with_two_numbers, with_one_number


@with_one_number
def my_sin(a):
    return sin(radians(a))


@with_one_number
def my_cos(a):
    return cos(radians(a))


@with_one_number
def my_tan(a):
    return tan(radians(a))


@with_one_number
def my_ctg(a):
    try:
        result = 1 / tan(radians(a))
    except ZeroDivisionError as e:
        print(f"Обнаружено деление на 0! Ошибка: {e}")
    else:
        return result


@with_one_number
def my_factorial(a):
    return factorial(int(a))


@with_one_number
def my_ln(a):
    try:
        result = log(a)
    except ValueError as e:
        print(f"Логарифма с аргументов {a} не существует! Ошибка: {e}")
    else:
        return result


@with_two_numbers
def my_gcd_and_lcm(a: float, b: float):
    # Надо взять модуль для расчетов НОД и НОК
    a = abs(a)
    b = abs(b)
    answer = list()
    if (not a.is_integer()) or (not b.is_integer()):
        print("Обнаружена дробная часть, числа автоматически переделаны \
в целые")
        a = int(a)
        b = int(b)

    # Блок нахождения НОД
    a_gcd = a
    b_gcd = b
    while (a_gcd != 0 and b_gcd != 0):
        if a_gcd == b_gcd:
            answer.append(a_gcd)
            break
        elif a_gcd > b_gcd:
            a_gcd -= b_gcd
        else:
            b_gcd -= a_gcd

    # Блок нахождения НОК
    answer.append((a * b) / answer[0])
    return answer


def convert_base():
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while True:
        try:
            from_base = int(input("Введите из какой системы \
счисления Вы переводите: "))
            n = int(
                input("Введите число в данной системе счисления: "),
                from_base
            )
            to_base = int(input("Введите в какую систему \
счисления перевести: "))
        except (ValueError, UnboundLocalError) as e:
            print(f"Произошла ошибка {e}. Все числа должны быть целыми, \
либо введенного числа не существует в системе счисления {from_base}")
            continue
        else:
            break

    while n > 0:
        result = digits[n % to_base] + result
        n = n // to_base
    return result


def find_square():
    try:
        n = int(input("Введите число сторон: "))
        a = float(input("Введите длину одно стороны: "))
    except ValueError as e:
        print(f"Произошла ошибка {e}. Вводите числа")
        return None
    else:
        square = n * a * a / 4 * (1 / tan(radians(180 / n)))
        return square


def solve_equation():
    while True:
        try:
            user_input = input("Введите все три коэффициента квадратного \
уравнения через пробел, либо 'exit'\n")
            if 'exit' in user_input.lower():
                return None
            a, b, c = map(float, user_input.split())
        except ValueError as e:
            print(f"Произошла ошибка {e}. Вводите числа")
        else:
            break

    D = b ** 2 - 4 * a * c
    if D < 0:
        real = -b / (2 * a)
        imaginary = sqrt(-D) / (2 * a)
        x1 = complex(real, imaginary)
        x2 = complex(real, -imaginary)
    else:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)

    if x1 == x2:
        return x1

    answer = [x1, x2]
    return answer
