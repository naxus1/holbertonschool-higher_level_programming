#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    size_len = len(argv)
    add = 0

    for i in range(1, size_len):
        number = int(argv[i])
        add = add + number
    print("{:d}".format(add))
