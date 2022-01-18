# https://github.com/ArtemNikolaev/gb-hw/issues/34
import io
from itertools import count

numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

fR = io.open('5.4.txt', 'r', encoding='utf-8')
fW = io.open('5.4-new.txt', 'w', encoding='utf-8')

counter = count()
string = fR.readline()

while len(string) > 0:
    print('Line: ', next(counter))
    print('\tReaded: ', string)

    engNum, num = string.split(' - ')
    result = numbers[engNum] + ' - ' + num

    print('\tWrited: ', result)

    fW.write(result)
    string = fR.readline()

fR.close()
fW.close()
