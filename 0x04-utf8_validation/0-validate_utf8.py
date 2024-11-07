#!/usr/bin/python3
"""Validates if a character is a valid utf-8 encoded structure"""


def validUTF8(data):
    """Validates a UTF-8 encoded data and returns false if it is false"""

    if data > 128:
        return 
