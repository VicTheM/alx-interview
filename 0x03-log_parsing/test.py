#!/usr/bin/python3

import re


ipSection = '^([0-9]{1,3}\.){3}[0-9]{1,3} \- (.+) "GET /projects/260 HTTP/1.1" [2-5]0[0134]$'

p = re.compile(ipSection)

p_addresses = [
    "192.168.1.1 - 324 \"GET /projects/260 HTTP/1.1\" 200",    # Valid
    "10.0.0.1",       # Valid
    "172.16.254.1",   # Valid
    "255.255.255.255",# Valid
    "0.0.0.0",        # Valid (represents "any" address)
    
    # Invalid IP addresses
    "256.100.50.25",  # Invalid (256 is out of range)
    "192.168.1",      # Invalid (missing one octet)
    "192.168.1.999",  # Invalid (999 is out of range)
    "123.456.78.90",  # Invalid (456 is out of range)
    "192.168.1.1.1",  # Invalid (too many octets)
    "192.168.01.1",   # Typically invalid (leading zero in an octet)
    "abc.def.ghi.jkl" # Invalid (non-numeric characters)
]


"""
for data in p_addresses:
    if p.match(data):
        print("Match found")
    else:
        print("\tx")
"""

print(p_addresses.pop())
