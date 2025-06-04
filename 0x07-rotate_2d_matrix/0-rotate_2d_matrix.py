#!/usr/bin/python3
"""
This module provides a function to rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of lists): The matrix to rotate.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            # Transpose the matrix
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        # Reverse each row
        row.reverse()
