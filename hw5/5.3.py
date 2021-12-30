# https://github.com/ArtemNikolaev/gb-hw/issues/33
from itertools import count
from utils import read_file

strings = read_file('5.3.txt')
salarySum = 0
peoples = 0

counter = count()
for string in strings:
    peoples = next(counter)
    name, salaryStr = string.split()
    # todo: after second dz merged check input with can_be_float
    salary = float(salaryStr)
    salarySum += salary
    if salary < 20000:
        print(string)


print('\nCредняя зарплата: ', salarySum / peoples)