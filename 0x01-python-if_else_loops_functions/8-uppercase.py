#!/usr/bin/python3
def uppercase(str):
    for letter in range(len(str)):
        new_letter = ord(str[letter])
        if new_letter > 96 and new_letter < 123:
            new_letter = new_letter - 32
        print('{:c}'.format(new_letter), end='')
    print()
