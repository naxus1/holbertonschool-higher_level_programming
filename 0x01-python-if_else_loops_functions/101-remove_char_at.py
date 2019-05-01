#!/usr/bin/python3
def remove_char_at(str, n):
    size_str = len(str)
    cont = 0;
    if n <= size_str and n >= 0:
        str = str[0:n] + str[n + 1:]
    return(str)
