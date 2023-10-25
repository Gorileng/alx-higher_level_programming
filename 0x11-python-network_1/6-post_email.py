#!/usr/bin/python3
"""The script that:
- take the URL and the email address
- send the POST request to a passed URL with an email as the parameter
- display a body of a response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
