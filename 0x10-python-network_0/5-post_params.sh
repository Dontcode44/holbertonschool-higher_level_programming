#!/bin/bash
# Write a Bash script that takes in a URL, sends a POST
curl -sX POST -d "$1" 'email=test@gmail.com' -F 'subject=I will always be here for PLD'
