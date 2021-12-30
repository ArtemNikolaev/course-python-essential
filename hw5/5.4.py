# https://github.com/ArtemNikolaev/gb-hw/issues/34
import io
from itertools import count
from utils import read_file

numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

fR = read_file('5.4.txt')
fW = io.open('5.4-result.txt', 'w', encoding='utf-8')

counter = count()

for string in fR:
    print('Line: ', next(counter))
    print('\tReaded: ', string)

    engNum, num = string.split(' - ')
    result = numbers[engNum] + ' - ' + num

    print('\tWrited: ', result)

    fW.write(result)

fW.close()
