def is_int(num):
    return isinstance(num, int)


def is_not_int(num):
    return not is_int(num)


def is_float(num):
    return isinstance(num, float)


def is_not_float(num):
    return not is_float(num)


def is_number(num):
    return is_int(num) or is_float(num)


def is_not_number(num):
    return not is_number(num)


def can_be_int(num):
    try:
        int(num)

        return True
    except ValueError:
        return False


def cant_be_int(num):
    return not can_be_int(num)


def can_be_float(num):
    try:
        float(num)

        return True
    except ValueError:
        return False


def cant_be_float(num):
    return not can_be_float(num)


def can_be_int_or_float(num):
    return can_be_int(num) or can_be_float(num)


def cant_be_int_or_float(num):
    return not can_be_int_or_float(num)

