# https://github.com/ArtemNikolaev/gb-hw/issues/35
import random
from functools import reduce


def reducer(summa, new_num):
    return summa + int(new_num)


def generate_file(filename):
    f = open(filename, 'w')

    number_amount = random.randrange(10, 100)

    for i in range(0, number_amount):
        f.write(str(random.randrange(1, 20)) + ' ')
    f.close()


def calculate_file(filename):
    f = open(filename, 'r')

    print(reduce(reducer, f.read().split(), 0))
    f.close()


file_name = '5.5.txt'
generate_file(file_name)
calculate_file(file_name)
