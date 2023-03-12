#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    if len(sys.argv) - 1!= 3:
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
        print("{} {} {} = {}".format(a, ops, b, calculator_1.add(a, b))
    elif ops == '-':
        print("{} {} {} = {}".format(a, ops, b, calculator_1.sub(a, b))
    elif ops == '/':
        print("{} {} {} = {}".format(a, ops, b, calculator_1.div(a, b))
    elif ops == '*':
        print("{} {} {} = {}".format(a, ops, b, calculator_1.sub(a, b))
