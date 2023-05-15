#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    division_sign = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            division_sign.append(True)
        else:
            division_sign.append(False)
    return (division_sign)

