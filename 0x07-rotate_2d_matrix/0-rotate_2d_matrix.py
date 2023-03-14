#!/usr/bin/env python3
"""
To rotate a 2D matrix by 90 degrees clockwise,
we need to transpose the matrix
    first and then reverse each row.
Transposing a matrix involves swapping
    elements across the diagonal,
so the element at row i and column j is
    swapped with the element at row j and column i.
Reversing each row is equivalent to swapping
    the elements at opposite ends of each row.
"""


def rotate_2d_matrix(matrix) -> None:
    """
    Rotate a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (List[List[int]]): a 2D matrix to be rotated.

    Returns:
        None. The matrix is edited in place.
    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
