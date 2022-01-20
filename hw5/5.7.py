# https://github.com/ArtemNikolaev/gb-hw/issues/37
from json import dumps
from utils import read_file


def calculate_result(strings):
    average_sum = 0
    average_count = 0
    firm_dict = {}

    for string in strings:
        name, trash, income, outcome = string.split()
        profit = float(income) - float(outcome)
        firm_dict[name] = profit
        if profit > 0:
            average_sum += profit
            average_count += 1
    return [
        firm_dict,
        {"average_profit": average_sum / average_count}
    ]


def save_result(filename, result):
    with open(filename, 'w') as opened_file:
        opened_file.write(
            dumps(result)
        )


def run(file_from, file_to):
    strings = read_file(file_from)
    result = calculate_result(strings)
    save_result(file_to, result)


run(file_from='5.7.txt', file_to='5.7.result.txt')
