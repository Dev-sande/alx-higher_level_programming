#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    
    for h in range(len(matrix)):
        
        for m in range(len(matrix[h])):
            if m != 0:
                print(" ", end='')
                
            print("{:d}".format(matrix[h][m]), end='')
            
        print()

