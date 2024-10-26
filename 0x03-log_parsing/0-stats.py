#!/usr/bin/python3
"""This file uses regular expression to parse a log file
and output a summary"""

import os
import sys
import signal
import re


def custom_print(size, data):
    """Prints a neat format"""
    print(f"File size: {size}")

    for code, number in data.items():
        if isinstance(number, int) and number > 0: 
            print(f"{code}: {number}")


log = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
        }
file_size = 0

# Get input of a certain format
pattern = '^([0-9]{1,3}\.){3}[0-9]{1,3} \- (.+) "GET /projects/260 HTTP/1.1" [2-5]0[0134] \d+$'
test = re.compile(pattern)

counter = 0
try:
    for line in sys.stdin:
        counter += 1
        if test.match(line):
            splitted = line.split()
            file_size += int(splitted.pop())
            code = splitted.pop()

            if code in log:
                log[code] += 1
        
        if counter == 10:
            counter = 0
            custom_print(file_size, log)
except KeyboardInterrupt:
    custom_print(file_size, log)
