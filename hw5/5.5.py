# https://github.com/ArtemNikolaev/gb-hw/issues/35
import random
from functools import reduce


def reducer(summa, newNum):
    return summa + int(newNum)


def generate_file():
    f = open('5.5.txt', 'w')

    number_amount = random.randrange(10, 100)

    for i in range(0, number_amount):
        f.write(str(random.randrange(1, 20)) + ' ')
    f.close()


def calculate_file():
    f = open('5.5.txt', 'r')

    print(reduce(reducer, f.read().split(), 0))
    f.close()


generate_file()
calculate_file()