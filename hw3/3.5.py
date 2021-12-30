# https://github.com/ArtemNikolaev/gb-hw/issues/5

import shared.number as num


def ask_stop_word():
    return input('Введите стоп-слово-символ: ')


def calculate(stop):
    result = 0
    arr = []

    while True:
        if len(arr) == 0:
            print('Текущая сумма: ' + str(result))
            arr = input('Введите строку чисел: ').split()
        el = arr.pop(0)
        if num.can_be_int_or_float(el):
            result += float(el)
        elif el == stop:
            break
        print('Итоговая сумма: ' + str(result))

    return result


def run():
    calculate(ask_stop_word())


run()
