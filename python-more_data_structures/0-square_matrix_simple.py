#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Yeni bir matris yaradırıq, hər elementin kvadratını hesablayırıq
    return [[x**2 for x in row] for row in matrix]
