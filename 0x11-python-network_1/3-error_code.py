#!/usr/bin/python3
# Python script that takes in URL and displays the body of the response

import sys
from urllib import request, error

if __name__ == "__main__":

    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as exeptionA:
        print('Error code: {}'.format(exeptionA.code))
