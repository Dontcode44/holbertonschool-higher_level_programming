#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email address,
sends a POST
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = requests.post(url, data={'email': sys.argv[2]})
    print(email.text)
