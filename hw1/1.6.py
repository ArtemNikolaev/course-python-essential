# https://github.com/ArtemNikolaev/gb-hw/issues/15

a = int(input('Введите a: '))
b = int(input('Введите b: '))
day = 1

while(a < b):
    day += 1
    a *= 1.1

print('День на который спортсмен достиг результата:', day)