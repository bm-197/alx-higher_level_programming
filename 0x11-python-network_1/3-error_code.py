#!/usr/bin/python3
"""cript that takes in a URL, sends a request to the
URL and displays the body of the response (decoded
in utf-8)."""

from urllib import request
from sys import argv

if __name__ == "__main__":
    data = parse.urlencode({"email": argv[2]}).encode('utf-8')
    with request.urlopen(argv[1], data) as page:
        print(page.read().decode('utf-8'))
