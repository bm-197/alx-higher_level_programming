#!/usr/bin/python3
def pow(a, b):
    product = 1
    for i in range(b):
        if b > 0:
            product *= a
        elif b < 0:
            product *= 1/a
    return product
