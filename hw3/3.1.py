# https://github.com/ArtemNikolaev/gb-hw/issues/9

import shared.typed_input as ti
import shared.number as number


def division(val1, val2):
    if number.is_not_number(val1) or\
            number.is_not_number(val2) or\
            val2 == 0:
        print('Numbers should be int or float and second number shoud not be equal 0')
        return
    return val1 / val2


def ask_for_data():
    val1 = ti.get_number('Введите первое число: ')
    val2 = None
    while not val2:
        temp_num2 = ti.get_number('Введите второе число, не равное 0: ')
        if not temp_num2 == 0:
            val2 = temp_num2
        else:
            print('Число не должно быть равно 0')
    return val1, val2


def print_division(val1, val2):
    print(division(val1, val2))


num1, num2 = ask_for_data()
print_division(num1, num2)
