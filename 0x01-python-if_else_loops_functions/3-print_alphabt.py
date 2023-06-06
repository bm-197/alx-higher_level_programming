#!/usr/bin/python3
for char in range(97, 123):
    if chr(char) is not 'q' and chr(char) is not 'e':
        print('{}'.format(chr(char)), end="")
