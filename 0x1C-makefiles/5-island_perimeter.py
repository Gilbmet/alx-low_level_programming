#!/usr/bin/python3

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list): a list of list of integers representing the island and water zones.

    Returns:
        int: the perimeter of the island.

    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # add 4 for a land cell
                perimeter += 4
                # subtract 2 for each adjacent land cell (up and left)
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    
    return perimeter
