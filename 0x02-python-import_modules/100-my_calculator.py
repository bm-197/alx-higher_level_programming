#!/usr/bin/python3
if __name__ == "__main__":
    form calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = ['+', '-', '/', '*']
    if sys.argv[2] not in list(op):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    ops = sys.argv[2]
    if ops == '+':
        print("{} {} {} = {}".format(a, ops, b, add(a, b))
    elif ops == '-':
        print("{} {} {} = {}".format(a, ops, b, sub(a, b))
    elif ops == '/':
        print("{} {} {} = {}".format(a, ops, b, div(a, b))
    elif ops == '*':
        print("{} {} {} = {}".format(a, ops, b, sub(a, b))
