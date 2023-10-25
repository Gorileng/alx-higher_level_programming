#!/usr/bin/python3
"""The script that:
- takes the URL,
- send the request to URL and display the value
- of X-Request-Id variable found in a header of a response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
