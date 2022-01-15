# https://github.com/ArtemNikolaev/gb-hw/issues/23
def run(array):
    return (
        array[i]
        for i in range(1, len(array))
        if array[i] > array[i-1]
        )


test_input = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print(list(run(test_input)))
