#!/usr/bin/python3
for a in range(10):
    for units in range(a+1, 10):
        print("{:d}{:d}".format(a, units), end="")
        if a != 8 or units != 9:
            print(", ", end="")
print()
