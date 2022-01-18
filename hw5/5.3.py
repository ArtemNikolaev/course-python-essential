# https://github.com/ArtemNikolaev/gb-hw/issues/33
import io
from itertools import count

def run():
    f = io.open('5.3.txt', 'r', encoding='utf-8')
    salarySum = 0
    peoples = 0

    string = f.readline()
    while len(string) > 0:
        peoples += 1

        name, salaryStr = string.split()
        # todo: after second dz merged check input with can_be_float
        salary = float(salaryStr)
        salarySum += salary
        if salary < 20000:
            print(string)
        string = f.readline()
    print('\nCредняя зарплата: ', salarySum / peoples)



run()
