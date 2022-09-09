#!/usr/bin/python3
# Write a Python script that fetches https://intranet.hbtn.io/status
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    re = res.read()
    print("Body response:")
    print("\t- type: {}".format(type(re)))
    print("\t- content: {}".format(re))
    print("\t- utf8 content: {}".format(re.decode("utf-8")))
