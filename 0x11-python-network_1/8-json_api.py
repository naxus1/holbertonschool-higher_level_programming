#!/usr/bin/python3
# Search API

import requests
from sys import argv

if __name__ == "__main__":

    value = {'q': '""'}
    if len(argv) == 2:
        value['q'] = argv[1]

    try:
        result = requests.post('http://0.0.0.0:5000/search_user', data=value)
        if result.json():
            j = result.json()
            print('[{}] {}'.format(j['id'], j['name']))
        else:
            raise NameError
    except ValueError:
        print("Not a valid JSON")
    except NameError:
        print("No result")
