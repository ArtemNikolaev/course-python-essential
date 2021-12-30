# https://github.com/ArtemNikolaev/gb-hw/issues/30

f = open('5.1.txt', 'w')
string = 'not empty string'

while len(string) > 0:
    string = input('Введите строку для записи или нажмите Enter для завершения: ')
    f.write(string + '\n')

f.close()
