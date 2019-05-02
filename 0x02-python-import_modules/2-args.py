#!/usr/bin/python3
from sys import argv

size_argv = len(argv)

if size_argv > 1:
    if size_argv - 1 == 1:
        print("{:d} argument:".format(size_argv - 1))
    else:
        print("{:d} arguments:".format(size_argv - 1))
    for i in range(1, size_argv):
        print("{}: {}".format(i, argv[i]))
else:
    print("{:d} arguments.".format(size_argv - 1))
