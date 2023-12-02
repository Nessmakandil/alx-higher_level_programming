#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for row in matrix:
        l = len(row)
        for i, col in enumerate(row):
            print("{:d}".format(col), end='\n' if i == l - 1 else ' ')
