# https://github.com/ArtemNikolaev/gb-hw/issues/22

from sys import argv, exit
from shared.number import can_be_float


def validate_arguments():
    if len(argv) < 4:
        print('Скрипт нужно запускать с тремя параметрами:')
        print('\t- отработанные часы')
        print('\t- часовая ставка')
        print('\t- премия')
        exit()


def to_number(value):
    if can_be_float(value):
        return float(value)
    else:
        print('Все параметры должны быть числовыми')
        exit()


def calculate_salary():
    validate_arguments()
    hours, rate, bonus = (to_number(argv[i]) for i in range(1, 4))

    return hours * rate + bonus


print(calculate_salary())