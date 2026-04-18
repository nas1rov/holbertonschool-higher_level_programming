#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    # Əgər arqument verilməyibsə q = "" olur
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': q}

    try:
        r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        # Cavabı JSON lüğəti kimi parse etməyə çalışırıq
        json_dict = r.json()

        if json_dict:
            print("[{}] {}".format(json_dict.get('id'), json_dict.get('name')))
        else:
            print("No result")

    except ValueError:
        # Əgər cavab düzgün formatda JSON deyilsə
        print("Not a valid JSON")
