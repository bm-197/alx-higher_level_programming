#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if letter >= 97 and letter_num <= 122:
            letter = chr(ord(letter) - 32)
        print('{}'.format(letter), end="")
    print("")

