#!/usr/bin/python3
# My Github!

import requests
import sys

if __name__ == "__main__":

    url = "https://api.github.com/users/" + sys.argv[1]
    logi = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    logi_dict = logi.json()
    print(logi_dict['id'])
