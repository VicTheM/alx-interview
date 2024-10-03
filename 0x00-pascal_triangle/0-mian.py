#!/usr/bin/python3
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    if len(triangle) == 0:
        print("Empty!")
    else:
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    for x in range(0, 4):
        print("---------------------------------------")
        print_triangle(pascal_triangle(x))
