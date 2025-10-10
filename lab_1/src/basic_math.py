from .decorators import with_two_numbers


@with_two_numbers
def my_sum(a, b):
    return a + b


@with_two_numbers
def my_sub(a, b):
    return a - b


@with_two_numbers
def my_mult(a, b):
    return a * b


@with_two_numbers
def my_div(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Обнаружено деление на 0! Ошибка: {e}")
    else:
        return result


@with_two_numbers
def my_raise(a, b):
    return a ** b
