#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    vox = 0
    for b in uniq_list:
        vox += b
    return (vox)

