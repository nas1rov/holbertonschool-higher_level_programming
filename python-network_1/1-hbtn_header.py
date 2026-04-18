#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    
    with urllib.request.urlopen(url) as response:
        # Extract the specific header value from the response
        request_id = response.headers.get('X-Request-Id')
        print(request_id)
