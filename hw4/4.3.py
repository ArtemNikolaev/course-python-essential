# https://github.com/ArtemNikolaev/gb-hw/issues/24

def multiple_of_20_21():
    return (i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0)


print(list(multiple_of_20_21()))
