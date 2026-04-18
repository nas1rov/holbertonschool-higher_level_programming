#!/usr/bin/python3
"""
Python script that takes 2 arguments (repository name and owner name)
and uses the GitHub API to list the 10 most recent commits.
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    # GitHub API URL-i son 10 commit-i gətirmək üçün formatlanır
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(url)
    commits = r.json()

    try:
        # Siyahıdan yalnız ilk 10 elementi götürürük
        for i in range(10):
            sha = commits[i].get('sha')
            author_name = commits[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, author_name))
    except IndexError:
        # Əgər cəmi 10-dan az commit varsa, proqram xəta vermədən dayansın
        pass
