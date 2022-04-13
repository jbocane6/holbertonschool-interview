#!/usr/bin/python3
triangle = []


def pascal_triangle(n):
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
    floor_list = [1, 1]
    size = len(floor) - 1

    for i in range(size):
        floor_list.insert(i + 1, floor[i] + floor[i + 1])
    return floor_list
