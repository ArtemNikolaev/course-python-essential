# https://github.com/ArtemNikolaev/gb-hw/issues/32
import io


f = io.open('5.2.txt', 'r', encoding='utf-8')
lines = f.readlines()
print('В файле ', len(lines), 'строк')
for i in range(0, len(lines)):
    words_amount = len(lines[i].split())
    print('\tВ ', i + 1, ' строке ', words_amount, 'слов')
    print('\t\t', lines[i])
f.close()
