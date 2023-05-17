#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order_o = list(a_dictionary.keys())
    order_o.sort()
    for b in order_o:
        print("{}: {}".format(b, a_dictionary.get(b)))

