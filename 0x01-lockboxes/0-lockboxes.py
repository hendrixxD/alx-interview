#!/usr/bin/python3
"""
task that determines if all boxes can be opened, given n boxes,
each box is numbered `0` to `n-1` and each may contain keys to the other boxes
"""


def canUnlockAll(boxes):
    """
    args:
        boxes -> list

    return -> bool (True/False)
    """
    # Set to store the keys we have seen
    keys = set()
    # Queue for storing keys that we need to process
    queue = []

    # Add the keys in the first box to the queue
    queue.extend(boxes[0])
    # Mark the first box as visited
    keys.add(0)

    # Process keys in the queue
    while queue:
        # Get a key from the queue
        key = queue.pop(0)
        # If the key corresponds to a box, add the box's keys to the queue
        # and mark the box as visited
        if key < len(boxes) and key not in keys:
            keys.add(key)
            queue.extend(boxes[key])

    # Return whether all boxes are visited or not
    return len(keys) == len(boxes)
