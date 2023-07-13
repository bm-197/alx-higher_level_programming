#!/usr/bin/python3
"""Define a function that creates a pascal tri."""


def pascal_triangle(n):
    """Return a pascal triangle.
    Args:
        n (int): number of rows for the pascal tri
    """
    if n <= 0:
        return []
    result = [[1]]

    for i in range(n - 1):
        tri = result[-1]
        row = [1]
        for j in range(i):
            row.append(tri[j] + tri[j + 1])
        row.append(1)
        result.append(row)
    return result
