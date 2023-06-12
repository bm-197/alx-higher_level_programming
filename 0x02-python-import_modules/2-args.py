#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    """number of and list of its arguments."""

    ind = len(sys.argv) - 1
    if ind == 1:
        print("0 arguments.")
    elif ind == 2:
        print("{} argument:".format(ind))    
    else:
        print("{} arguments:".format(ind))
    for i in range(1, ind):
        print("{}: {}".format(i, sys.argv[i]))
