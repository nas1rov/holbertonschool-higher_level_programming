#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8).
"""
import sys
import urllib.parse
import urllib.request
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    # Prepare the data to be sent in the POST request
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii') # Data should be bytes
    # Create the request object and send it
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
