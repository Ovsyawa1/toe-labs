from .globals import print_error_message


def create_two_numbers():
    while True:
        try:
            user_input = input("Введите два числа через пробел, либо \
'exit' для выхода: ")
            if 'exit' in user_input.lower():
                return None, None
            a, b = map(float, user_input.split())
            print(f"Вы ввели: {a:.3g} и {b:.3g}")
        except ValueError as e:
            print_error_message(e)
        else:
            return a, b


def with_two_numbers(func):
    def wrapper():
        a, b = create_two_numbers()
        if a is None or b is None:
            return None
        return func(a, b)
    return wrapper


def create_one_number():
    while True:
        try:
            user_input = input("Введите число, либо 'exit' для выхода: ")
            if 'exit' in user_input.lower():
                return None
            a = float(user_input)
            print(f"Вы ввели: {a:.3g}")
        except ValueError as e:
            print_error_message(e)
        else:
            return a


def with_one_number(func):
    def wrapper():
        a = create_one_number()
        if a is None:
            return None
        return func(a)
    return wrapper
