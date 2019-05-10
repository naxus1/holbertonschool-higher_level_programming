#!/usr/bin/python3
def roman_to_int(roman_string):
    dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}

    if roman_string is None:
        return (0)
    num_ant = 0
    suma = 0
    for number in roman_string:
        if dict_roman.get(number) <= num_ant:
            suma += dict_roman.get(number)
        else:
            suma += (dict_roman.get(number) - (2 * num_ant))
        num_ant = dict_roman.get(number)
    return suma
