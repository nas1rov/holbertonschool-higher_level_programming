#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Print the number with a trailing space if it's NOT the last element
            if i != len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                # Print the last number without a trailing space
                print("{:d}".format(row[i]), end="")
        # Move to a new line after each row
        print()
