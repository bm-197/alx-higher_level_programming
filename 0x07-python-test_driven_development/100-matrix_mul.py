#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices.

    Args:
        m_a (list): first matrix
        m_b (list): second matrix
    Return:
        the multiplied version of the two
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")


    m_b_t = []
    for i in range(len(m_b[0])):
        tmp_m = []
        for j in range(len(m_b[i])):
            tmp_m.append(m_b[j][i])
        m_b_t.append(tmp_m)
    new_m = []
    for i in m_a:
        tmp_m_2 = []
        for j in m_b_t:
            result = 0
            for k in range(len(j)):
                result += i[k] * j[k]
            tmp_m_2.append(result)
        new_m.append(tmp_m_2)
    return new_m
