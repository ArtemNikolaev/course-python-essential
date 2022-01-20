# https://github.com/ArtemNikolaev/gb-hw/issues/36
import re
from functools import reduce
from utils import read_file


def parse_line(string):
    return \
        re.findall(r'(\w+):', string)[0],\
        re.findall(r'\d+', string)


def run(filename):
    strings = read_file(filename)

    result = {}
    for string in strings:
        name, hoursArr = parse_line(string)
        amount = reduce(lambda a, b: float(a) + float(b), hoursArr)
        result[name] = amount

    return result


print(run('5.6.txt'))
