#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    lgnd = a_dictionary.copy()
    mki = list(lgnd.keys())

    for a in mki:
        lgnd[a] *= 2

    return (lgnd)

