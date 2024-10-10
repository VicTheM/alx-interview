#!/usr/bin/python3
"""
This file uses graph algorithm to solve lockboxes

BFS
"""


def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.

    The function determines if all boxes can be opened
    """
    # Queue for visited boxes
    keys = set()

    # Initially mark all the vertices as not visited
    # When we push a vertex into the q, we mark it as
    # visited
    numberOfBoxes = len(boxes)
    visited = [False] * numberOfBoxes

    # Mark the source node as visited and enqueue it
    visited[0] = True
    for x in boxes[0]:
        keys.add(x)

    # Iterate over the queue
    while keys:
        # Dequeue a vertex from queue and print it
        curr = keys.pop()

        # Get all adjacent vertices of the dequeued
        # vertex. If an adjacent has not been visited,
        # mark it visited and enqueue it
        if curr < numberOfBoxes and not visited[curr]:
            visited[curr] = True
            for x in boxes[curr]:
                keys.add(x)

    for truth in visited:
        if not truth:
            return False

    return True
