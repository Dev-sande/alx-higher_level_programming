#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)

    a = 0
    rep_laced = my_string[:]
    for h in range(length):
        if (my_string[h] == 'c' or my_string[h] == 'C'):
            new_string = rep_laced[:(h - a)] + my_string[(h + 1):]
            a += 1
    return (rep_laced)

