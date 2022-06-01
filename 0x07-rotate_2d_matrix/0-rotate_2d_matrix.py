#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    First, we made a address copy of the original matrix
    Next, We take the item at the position column and create a row with them
    then will assign that row to the original matrix
    """
    matrix_copy = matrix.copy()
    for column in range(len(matrix)):
        matrix[column] = [row[column] for row in reversed(matrix_copy)]
