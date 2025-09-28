from decorators import with_two_numbers, with_one_number


@with_two_numbers
def bitwise_and(a, b):
    return int(a) & int(b)


@with_two_numbers
def bitwise_or(a, b):
    return int(a) | int(b)


@with_two_numbers
def bitwise_xor(a, b):
    return int(a) ^ int(b)


@with_one_number
def bitwise_not(a):
    a = int(a)
    return ~a


@with_two_numbers
def bitwise_to_left(a, n):
    return int(a) << int(n)


@with_two_numbers
def bitwise_to_right(a, n):
    return int(a) >> int(n)
