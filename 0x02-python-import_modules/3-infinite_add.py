#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    """result of the addition of all arguments"""

    result = 0
    for i in range(1, len(sys.argv) + 1):
        result+=int(sys.argv[i])

    print(result)