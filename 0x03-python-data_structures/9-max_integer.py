#!/usr/bin/python3
def max_integer(my_list=[]):
    ln = len(my_list)
    if ln == 0:
        return (None)
    max_int = my_list[0]
    for a in range(1, ln):
        if my_list[a] > max_int:
            max_int = my_list[a]
    return (max_int)

