# https://github.com/ArtemNikolaev/gb-hw/issues/26
from functools import reduce


def even_100_1000():
    return (i for i in range(100, 1001) if i % 2 == 0)


def multiply():
    return reduce(lambda a, b: a * b, even_100_1000())


print(multiply())
