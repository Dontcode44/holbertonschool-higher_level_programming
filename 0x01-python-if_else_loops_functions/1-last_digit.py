#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    lastdigi = number % 10
else:
    tmp = number * -1
    lastdigit = (tmp % 10) * -1
if lastdigit > 5:
    print(f"Last digit of {number} is {lastdigi} and is greater than 5")
elif lastdigit == 0:
    print(f"Last digit of {number} is {lastdigi} and is 0")
else:
    print(f'Last digit of {number} is {lastdigi} and is less than 6 and not 0')
