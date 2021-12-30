# https://github.com/ArtemNikolaev/gb-hw/issues/17

listLen = int(input('Введите длину массива: '))
list = []
for i in range(0, listLen):
    list.append(input('Введите list[' + str(i) + ']: '))

print('List before change')
print(list);

rangeEnd = listLen - 1 if listLen % 2 == 0 else listLen - 2
for i in range(0, rangeEnd):
    list[i], list[i+1] = list[i+1], list[i]

print('List after change')
print(list);
