#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

def perform_operation(operation, a, b):
    if operation == 'add':
        return add(a, b)
    elif operation == 'sub':
        return sub(a, b)
    elif operation == 'mul':
        return mul(a, b)
    elif operation == 'div':
        return div(a, b)
    else:
        raise ValueError('Invalid operation')

if __name__ == '__main__':
    a = 10
    b = 5
    operations = ['add', 'sub', 'mul', 'div']
    for op in operations:
        result = perform_operation(op, a, b)
        print(f'{a} {op} {b} = {result}')

