#!/usr/bin/python3
"""module to validate UTF-8 encoding"""


def validUTF8(data):
    """
    Check if a list of integers represents a valid UTF-8 encoding.
    """
    num_bytes = 0

    for byte in data:
        byte = byte & 0xFF

        if num_bytes == 0:

            mask = 0b10000000
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:

            if not (byte & 0b10000000 and not (byte & 0b01000000)):
                return False

        num_bytes = num_bytes - 1 if num_bytes else 0

    return num_bytes == 0
