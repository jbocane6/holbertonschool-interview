#!/usr/bin/python3
"""Returns the perimeter of the island described in grid."""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid.
    Args:
        grid (list of list of int): 0 represents water, 1 represents land.
    Returns:
        int: Perimeter of the island.
    """

    perimeter = 0
    for row in range(len(grid)):
        for sq_perimeter in range(len(grid[row])):
            if grid[row][sq_perimeter] == 1:
                perimeter_sq = 4
                if sq_perimeter - 1 >= 0 and grid[row][sq_perimeter - 1] == 1:
                    perimeter_sq -= 1
                if sq_perimeter + 1 < len(grid[row])and grid[row][
                        sq_perimeter + 1] == 1:
                    perimeter_sq -= 1
                if row - 1 >= 0 and grid[row - 1][sq_perimeter] == 1:
                    perimeter_sq -= 1
                if row + 1 < len(grid) and grid[row + 1][sq_perimeter] == 1:
                    perimeter_sq -= 1
                perimeter += perimeter_sq
    return perimeter
