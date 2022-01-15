# https://github.com/ArtemNikolaev/gb-hw/issues/28

def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result

def run(n):
    for i in fact(n):
        print(i)


run(4)
