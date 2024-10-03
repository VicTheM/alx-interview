#!/usr/bin/python3

def pascal_triangle(n):
    """This function returns a list of lists
    that represent the pascla triangle of n"""
    
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    
    current = [1]
    triangle = [current]

    for x in range(1, n + 1):
        prev = triangle[-1]
        if len(prev) == 1:
            current = [1, 1]
        else:
            current = [1]
            for y in range(1, len(prev)):
                current.append(prev[y-1] + prev[y])
            current.append(1)

        triangle.append(current)

    return triangle
