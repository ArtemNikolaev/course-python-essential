# https://github.com/ArtemNikolaev/gb-hw/issues/25
def run(array):
    return [array[i] for i in range(0, len(array)) if array.count(array[i]) == 1]


test_case = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(run(test_case))
