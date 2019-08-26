#!/usr/bin/python3
# Error code #1

import requests
import sys

if __name__ == "__main__":
    result = requests.get(sys.argv[1])
    if result.status_code == requests.codes.ok:
        print(result.text)
    else:
        print("Error code: {}".format(result.status_code))
