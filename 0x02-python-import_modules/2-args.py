#!/usr/bin/python3
form sys import *
if not argv[1]:
    print('0 arguments.')
if argv[1] and len(argv) == 2:
    print('1 argument:')
else:
     print('{} arguments:'.foramt(len(argv) - 1))
for i in range(1, len(argv)):
    print('{}: {}'.format(i, argv[i]))
