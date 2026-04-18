#!/usr/bin/python3
"""
Uses Basic Authentication with a personal access token to access
GitHub user information and display the user id.
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]  # Bu sizin Personal Access Tokeninizdir
    # GitHub API-da istifadəçi məlumatlarını gətirən endpoint
    url = "https://api.github.com/user"
    # HTTPBasicAuth obyektindən istifadə edərək sorğu göndəririk
    auth = HTTPBasicAuth(username, password)
    r = requests.get(url, auth=auth)
    try:
        json_dict = r.json()
        # Əgər JSON boşdursa və ya ID yoxdursa None çap edirik
        print(json_dict.get('id'))
    except ValueError:
        print("None")
