#!/usr/bin/python3
# Write a Python script that fetches https://intranet.hbtn.io/status
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
    doc = res.read()
    print("Body response:")
    print("\t- type: {}".format(type(doc)))
    print("\t- content: {}".format(doc))
    print("\t- utf8 content: {}".format(doc.decode("utf-8")))
