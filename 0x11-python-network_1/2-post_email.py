#!/usr/bin/python3
# Python script that takes in a URL and an email, sends a POST to email

from urllib import parse, request
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    values = {"email": email}
    data = parse.urlencode(values).encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
    print(the_page)
