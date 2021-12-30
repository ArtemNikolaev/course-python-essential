# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в
# виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции
# возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью
# оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

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
