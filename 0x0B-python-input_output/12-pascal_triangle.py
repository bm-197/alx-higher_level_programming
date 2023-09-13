#!/usr/bin/python3
"""Pascal Triangle."""


def pascal_triangle(n):
    """Represetn a pascal triangle of n size

    Return:
         list of lists of integers representing triangle.
    """
    tri = [[1], [1,1]]

    for i in range(n-2):
        row = [1]
        for j in range(i+1):
            val = tri[i+1][j] + tri[i+1][j+1]
            row.append(val)
        row.append(1)
        tri.append(row)

    return tri
