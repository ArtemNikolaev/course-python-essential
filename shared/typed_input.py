from . import number


def get_int(msg):
    value = None
    while not value:
        temp_value = input(msg)
        if number.can_be_int(temp_value):
            value = int(temp_value)
        else:
            print('Input should be int')
    return value


def get_float(msg):
    value = None
    while not value:
        temp_value = input(msg)
        if number.can_be_float(temp_value):
            value = float(temp_value)
        else:
            print('Input should be float')
    return value


def get_number(msg):
    value = None
    while not value:
        temp_value = input(msg)

        if number.can_be_int(temp_value):
            value = int(temp_value)
        elif number.can_be_float(temp_value):
            value = float(temp_value)
        else:
            print('Input should be int or float')
    return value
