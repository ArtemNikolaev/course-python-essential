# https://github.com/ArtemNikolaev/gb-hw/issues/4

import shared.number as num
import shared.typed_input as ti


def my_func(x, y):
    if num.is_not_number(x) or\
            num.is_not_int(y) or\
            x <= 0 or y >= 0:
        print('Some of values are incorrect')
        return

    y *= -1

    while y > 1:
        x *= x
        y -= 1

    return 1 / x


def print_my_func(x, y):
    print(my_func(x, y))


def run():
    x = None
    y = None
    while num.is_not_number(x) or x <= 0:
        x = ti.get_number('Введите действительное положительное число: ')
    while num.is_not_int(y) or y >= 0:
        y = ti.get_int('Введите целое отрицательное число:')
    print_my_func(x, y)


run()
