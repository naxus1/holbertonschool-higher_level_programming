#!/usr/bin/python3
# Python script that takes in a URL and displays the value of the X-Request-Id

import sys
import urllib.request

if __name__ == "__main__":

    fetch_url = sys.argv[1]
    with urllib.request.urlopen(fetch_url) as response:
        content = response.info()
        print(content["X-Request-Id"])
