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

