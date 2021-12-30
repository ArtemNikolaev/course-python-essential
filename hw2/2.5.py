# https://github.com/ArtemNikolaev/gb-hw/issues/20

rating = [7, 5, 3, 3, 2]
print('Rating is: ' + str(rating))
num = int(input('num: '))

while (num or num == 0):
    rating.append(num)
    rating.sort()
    rating.reverse()

    print('Rating is: ' + str(rating))

    num = int(input('num: '))

