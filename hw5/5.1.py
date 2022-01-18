# https://github.com/ArtemNikolaev/gb-hw/issues/30

def run():
    f = open('5.1.txt', 'w')
    str = 'not empty string'

    while(len(str) > 0):
        str = input('Введите строку для записи или нажмите Enter для завершения: ')
        f.write(str + '\n')

    f.close()

run()
