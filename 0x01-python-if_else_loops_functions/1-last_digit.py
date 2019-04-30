#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    result = ((-number) % 10) * -1
else:
    result = (number) % 10

if result > 5:
    print("Last digit of {} is {} and is greater than5".
          format(number, result))

elif result == 0:
    print("Last digit of {} is {} and is 0".format(number, result))

if result < 6 and result != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".
          format(number, result))
