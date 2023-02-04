#!/usr/bin/python3
"""
 Lockboxes
"""


def canUnlockAll(boxes):
    """
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers

    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    """
    n = len(boxes)
    keys = set([0])
    for i in range(n):
        if i in keys:
            for j in boxes[i]:
                keys.add(j)
    return n == len(keys)
