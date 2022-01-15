# https://github.com/ArtemNikolaev/gb-hw/issues/27
from shared.number import is_not_int
from sys import exit


def int_generator(value):
    if is_not_int(value):
        print('Cтартовое значение должно быть целым')
        exit()
    while True:
        yield value
        value += 1


def test_int_generator():
    for i in int_generator(100):
        if i > 1000:
            exit()
        print(i)


test_int_generator()
