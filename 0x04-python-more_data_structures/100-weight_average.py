#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    top = 0
    btm = 0
    for tup in my_list:
        top += tup[0] * tup[1]
        btm += tup[1]
    return (top / btm)

