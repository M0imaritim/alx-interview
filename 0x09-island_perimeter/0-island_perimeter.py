#!/usr/bin/python3
"""Module to calculate the perimeter of an island in a grid."""


def island_perimeter(grid):
    """
    Return the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D grid where 1 is land and 0 is water.

    Return:
        int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
