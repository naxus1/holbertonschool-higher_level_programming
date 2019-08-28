#!/usr/bin/python3
# Time for an interview!

import requests
import sys

if __name__ == "__main__":

    owner = sys.argv[1]
    repo = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    html = requests.get(url)
    list_commits = html.json()

    for i in range(10):
        commit = list_commits[i]
        sha = commit["sha"]
        author = commit["commit"]["author"]["name"]
        print("{}: {}".format(sha, author)
