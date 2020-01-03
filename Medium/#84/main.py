"""
Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""

import numpy as np


def sinkIsland(grid: np.ndarray, y: int, x: int) -> None:
	grid[y][x] = False

	if y > 0 and grid[y - 1][x]:
		sinkIsland(grid, y - 1, x)

	if x + 1 < grid.shape[1] and grid[y][x + 1]:
		sinkIsland(grid, y, x + 1)

	if y + 1 < grid.shape[0] and grid[y + 1][x]:
		sinkIsland(grid, y + 1, x)

	if x > 0 and grid[y][x - 1]:
		sinkIsland(grid, y, x - 1)


def nbIslands(grid: np.ndarray) -> int:
	islands = 0

	for (y, x), cell in np.ndenumerate(grid):
		if cell:
			sinkIsland(grid, y, x)
			islands += 1

	return islands


grid = np.array([[True, False, False, False, False],
                 [False, False, True, True, False],
                 [False, True, True, False, False],
                 [False, False, False, False, False],
                 [True, True, False, False, True],
                 [True, True, False, False, True]])
print(f"nbIslands(grid) = {nbIslands(grid)}")
