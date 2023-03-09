#!/usr/bin/python3
letter_num = 0
def uppercase(str):
    for letter in str:
        letter_num = ord(letter)
        if letter >= 97 and letter_num <= 122:
            letter_num -= 32
            letter = chr(letter_num)
            print('{}'.format(letter), end="")
        else:
            print('{}'.format(letter), end = "")

