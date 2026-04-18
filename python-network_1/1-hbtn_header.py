#!/usr/bin/python3
"""
Takes in a URL, sends a request, and displays the value 
of the X-Request-Id variable found in the header.
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        # Get the headers from the response
        headers = response.info()
        # Display the value of the specific header
        print(headers.get('X-Request-Id'))
