#!/usr/bin/python3


if __name__ == "__main__":
    """result of the addition of all arguments"""
    import sys

    result = 0
    for i in range(1, len(sys.argv)):
        result+=int(sys.argv[i])
    print(result)
