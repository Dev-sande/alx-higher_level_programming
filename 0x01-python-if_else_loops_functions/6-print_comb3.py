#!/usr/bin/python3
for num in range(0, 90):
    if num % 10 > num // 10:
        print(f"{num:02d}", end='')
        if num != 89 and num % 10 > num // 10:
            print(', ', end='')
print()
