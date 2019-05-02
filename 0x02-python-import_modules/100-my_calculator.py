#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == '__main__':

    size_argv = len(argv) - 1
    if size_argv == 3:
        num1 = int(argv[1])
        num2 = int(argv[3])
        if argv[2] == "+":
            print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
        elif argv[2] == "-":
            print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
        elif argv[2] == "*":
            print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
        elif argv[2] == "/":
            print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
