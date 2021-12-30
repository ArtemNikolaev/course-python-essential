# https://github.com/ArtemNikolaev/gb-hw/issues/6

def int_function(string):
    if not isinstance(string, str):
        print('Значение должно быть строкой')
        return
    return string.capitalize()


def capitalize_words(string):
    str_arr = string.split()
    result = ''
    length = len(str_arr)
    for i in range(0, length):
        result += int_function(str_arr[i])
        if i < length - 1:
            result += ' '
    return result


def run():
    string = input('Введите строку в нижнем регистре: ')
    print(capitalize_words(string))


run()
