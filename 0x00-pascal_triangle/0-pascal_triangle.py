#!/usr/bin/python3
"""pascals triangle"""


def pascal_triangle(n):
    """git
    a function that returns a list
    of integers representing the
    pascal triangle of n:
       . Returns an empty list if n <= 0
       . assume n will be always an integer
    """
    try:
        # assume n will be always an integer
        if isinstance(n, int):
            if n <= 0:
                return []
            if n == 1:
                return [[1]]

            result = []
            for i in range(n):
                row = []
                for j in range(i + 1):
                    if j == 0 or j == i:
                        row.append(1)
                    else:
                        row.append(result[i-1][j-1] + result[i-1][j])
                result.append(row)
            return result
    except ValueError as e:
        print(e)
