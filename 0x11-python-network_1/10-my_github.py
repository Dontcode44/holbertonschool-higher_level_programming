#!/usr/bin/python3
"""
Write a Python script that takes your GitHub
credentials (username and password)
"""
import requests
import sys


if __name__ == "__main__":
    basic = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    url = requests.get("https://api.github.com/user", request.auth=basic)
    status, id_ = url.status_code, url.json().get("id")
    print('None') if status >= 400 else print(id_)
