#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status

import urllib.request

if __name__ == "__main__":

    featch_url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(featch_url) as response:
        content = response.read()
        content_type = type(content)
        content_utf8 = content.decode("utf-8")
        print("Body response:")
        print("\t - type: {}".format(content_type))
        print("\t - content: {}".format(content))
        print("\t - utf8 content: {}".format(content_utf8))
