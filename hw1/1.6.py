# Sportsmen
# a=2 b=3, result = 6

a = int(input('Введите a: '))
b = int(input('Введите b: '))
day = 1

while(a < b):
    day += 1
    a *= 1.1

print('День на который спортсмен достиг результата:', day)