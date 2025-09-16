#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
        There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    Determines if boxes can be opened.
    Args: boxes (List): List of Lists of integers
        Returns:
            (bool): Tells whether all items in the list can be opened
    """
    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = 0
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False
