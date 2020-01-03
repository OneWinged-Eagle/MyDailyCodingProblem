"""
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B

Becomes

B B G
G G G
G G G
B B B
"""

import numpy as np
from typing import Tuple

def fill(grid: np.ndarray, loc: Tuple[int, int], colour: str, prev: str = None) -> np.ndarray:
	x, y = loc

	if x < 0 or x >= grid.shape[1] or y < 0 or y >= grid.shape[0] or (prev != None and grid[y][x] != prev):
		return grid

	grid[y][x], prev = colour, grid[y][x]

	fill(grid, (x, y - 1), colour, prev)
	fill(grid, (x + 1, y), colour, prev)
	fill(grid, (x, y + 1), colour, prev)
	fill(grid, (x - 1, y), colour, prev)

	return grid

grid = np.array([['B', 'B', 'W'], ['B', 'W', 'W'],
                  ['W', 'B', 'W'], ['B', 'B', 'W'], ['W', 'W', 'B']])
print(f"grid = \n{grid}")
print(f"fill(grid, (2, 2), 'G') = \n{fill(grid, (2, 2), 'G')}")
print(f"fill(grid, (2, 4), 'W') = \n{fill(grid, (2, 4), 'W')}")
print(f"fill(grid, (2, 4), 'G') = \n{fill(grid, (2, 4), 'G')}")
