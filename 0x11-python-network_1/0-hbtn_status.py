#!/usr/bin/python3
"""
Script: Fetches a website and show the response
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()

    print("Body response:\n\
\t- type: {}\n\
\t- content: {}\n\
\t- utf8 content: {}".format(type(html), html, html.decode("utf-8")))
