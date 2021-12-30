# https://github.com/ArtemNikolaev/gb-hw/issues/19

str = input('Введите предложение: ')
strList = str.split()

for i in range(0, len(strList)):
    if len(strList[i]) > 10 :
        strList[i] = strList[i][0:10] + '...'
    print(i + 1, strList[i])