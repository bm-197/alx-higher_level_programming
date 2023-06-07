#!/usr/bin/python3


def print_last_digit(number):
    """print the last digit of a number"""
    last_digit = abs(number) % 10
    if number < 0:
        last_digit = - last_digit
    return last_digit
