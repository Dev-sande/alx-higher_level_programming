#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    va_r = len(tuple_a)
    var_2 = len(tuple_b)

    if va_r == 0:
        cr = 0
        ct = 0
    elif va_r == 1:
        cr = tuple_a[0]
        ct = 0
    else:
        cr = tuple_a[0]
        ct = tuple_a[1]

    if var_2 == 0:
        ch = 0
        cx = 0
    elif var_2 == 1:
        ch = tuple_b[0]
        cx = 0
    else:
        ch = tuple_b[0]
        cx = tuple_b[1]
    new_tuple = (cr + ch, ct + cx)
    return (new_tuple)

