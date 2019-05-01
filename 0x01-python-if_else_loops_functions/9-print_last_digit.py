#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    a = number % 10
    print(a, end='')
    return(a)
