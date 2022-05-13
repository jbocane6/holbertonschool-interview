#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore
    you only need to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    nbrOfbytes = 0
    for i in data:
        mask = 1 << 7
        if nbrOfbytes == 0:
            while mask & i:
                nbrOfbytes += 1
                mask >>= 1
            if nbrOfbytes == 0:
                continue
            elif nbrOfbytes == 1 or nbrOfbytes > 4:
                return False
        else:
            if not (i & 1 << 7 and not (i & 1 << 6)):
                return False
        nbrOfbytes = nbrOfbytes - 1
    if nbrOfbytes == 0:
        return True
    return False

def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
    count = 0
    for c in data:
        if count == 0:
            if (c >> 5) == 0b110:
                count = 1
            elif (c >> 4) == 0b1110:
                count = 2
            elif (c >> 3) == 0b11110:
                count = 3
            elif (c >> 7):
                return False
        else:
            if (c >> 6) != 0b10:
                return False
        count -= 1
    return count == 0