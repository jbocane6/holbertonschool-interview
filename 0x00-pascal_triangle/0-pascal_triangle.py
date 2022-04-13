#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal's triangle of n:
"""
triangle = []


def pascal_triangle(n):
    """
    Return a list of lists, or a null list if n <=0
    """
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        triangle.append(pascal_triangle(n - 1))
        return triangle.append([1, 1])
    else:
        pascal_triangle(n - 1)
        triangle.append(get_floor(triangle[n - 2]))
        return triangle


def get_floor(floor):
    """
    Creates the triangle's floor
    """
    floor_list = [1, 1]
    size = len(floor) - 1

    if size > 0:
        for i in range(size):
            floor_list.insert(i + 1, floor[i] + floor[i + 1])
    return floor_list