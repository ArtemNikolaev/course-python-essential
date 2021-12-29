def is_int(num):
    try:
        int(num)

        return True
    except ValueError:
        return False


def is_not_int(num):
    return not is_int(num)


def is_float(num):
    try:
        float(num)

        return True
    except ValueError:
        return False


def is_not_float(num):
    return not is_float(num)


def is_int_or_float(num):
    return is_int(num) and is_float(num)


def is_not_int_or_float(num):
    return not is_int_or_float(num)

