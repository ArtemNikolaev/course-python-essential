# https://github.com/ArtemNikolaev/gb-hw/issues/27
from shared.number import is_not_int
from sys import exit
from itertools import cycle, count


# итератор, генерирующий целые числа, начиная с указанного;
def int_generator(from_value, to_value):
    if is_not_int(from_value):
        print('Cтартовое значение должно быть целым')
        exit()
    while from_value <= to_value:
        yield from_value
        from_value += 1


def test_int_generator():
    print('Result for int generator')
    for i in int_generator(from_value=100, to_value=105):
        print('\t', i)


# итератор, повторяющий элементы некоторого списка, определённого заранее.
def list_repeater(array, index_from, index_to, repeat_times):
    counter = count(1, 1)
    for i in cycle(array[index_from:index_to+1]):
        if next(counter) == repeat_times:
            return i
        else:
            yield i


def test_list_repeater():
    print('Result for int generator')
    test_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i in list_repeater(
        array=test_list,
        index_from=1,
        index_to=7,
        repeat_times=15
    ):
        print('\t', i)


# run tests
test_int_generator()
test_list_repeater()
