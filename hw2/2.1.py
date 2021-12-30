# https://github.com/ArtemNikolaev/gb-hw/issues/16

list = [1, 2.0, 'bla', [1, 2], (1, 2), {'a': 'bla'}, {1, 0, 2}]

for listEl in list:
    print(type(listEl))
