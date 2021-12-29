# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

import shared.typed_input as ti

def my_func(arg1, arg2, arg3):
    return arg1 + arg2 + arg3 - min([arg1, arg2, arg3])


def ask_parameters():
    num1 = ti.get_number('Введите первое число: ')
    num2 = ti.get_number('Введите второе число: ')
    num3 = ti.get_number('Введите третье число: ')
    return num1, num2, num3


def run():
    num1, num2, num3 = ask_parameters()
    print(my_func(num1, num2, num3))


run()