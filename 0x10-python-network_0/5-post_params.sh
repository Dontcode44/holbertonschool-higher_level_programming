#!/bin/bash
# Write a Bash script that takes in a URL, sends a POST
curl -sX POST --data "$1" 'email=test@gmail.com&subject=I will always be here for PLD'
