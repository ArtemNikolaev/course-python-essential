# https://github.com/ArtemNikolaev/gb-hw/issues/13

num = int(input('Введите число: '))
max = 0

while num != 0:
    last = num % 10
    num = num // 10
    if last > max:
        max = last
        if max == 9:
            break

print(max)