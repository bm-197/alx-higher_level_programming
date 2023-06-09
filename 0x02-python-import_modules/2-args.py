#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    """number of and list of its arguments."""

    ind = len(sys.argv)
    if ind == 1:
        print("0 arguments.")
    elif ind == 2:
        print("{} argument:".format(ind - 1))    
    else:
        print("{} arguments:".format(ind - 1))
    for i in range(1, ind + 1):
        print("{}: {}".format(i, sys.argv[i]))
