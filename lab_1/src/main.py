from .globals import print_error_message, START_MESSAGE
from .basic_math import my_sum, my_sub, my_mult, my_div, my_raise
from .advanced_math import (
    my_sin, my_cos, my_tan, my_ctg, my_factorial, my_ln,
    my_gcd_and_lcm, convert_base, find_square, solve_equation
)
from .bitwise_operations import (
    bitwise_and, bitwise_or, bitwise_xor, bitwise_not,
    bitwise_to_left, bitwise_to_right
)


def main():
    switch_dict = {
        1: my_sum,
        2: my_sub,
        3: my_mult,
        4: my_div,
        5: my_raise,
        6: my_sin,
        7: my_cos,
        8: my_tan,
        9: my_ctg,
        10: bitwise_and,
        11: bitwise_or,
        12: bitwise_xor,
        13: bitwise_not,
        14: bitwise_to_left,
        15: bitwise_to_right,
        16: my_factorial,
        17: my_ln,
        18: my_gcd_and_lcm,
        19: convert_base,
        20: find_square,
        21: solve_equation,
    }

    while True:
        try:
            option = input(START_MESSAGE)
            if 'exit' in option.lower():
                return 0
            option = int(option)
        except ValueError as e:
            print_error_message(e)
        else:
            if (option >= 6 and option <= 9):
                print("Введите значение в градусах")
            break

    answer = switch_dict[option]()
    if answer:
        if isinstance(answer, str):
            print(f"Ответ: {answer}")
        elif isinstance(answer, list):
            print("Ответы:", end=" ")
            for x in answer:
                print(f"{x:.5g}", end=" ")
        else:
            print(f"Ответ: {answer:.5g}")


if __name__ == "__main__":
    main()
