"""
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
"""

import numpy as np


def clockwise(grid: np.ndarray) -> None:
	if grid.size == 0:
		return

	for x in range(grid.shape[1]):
		print(grid[0][x])

	for y in range(1, grid.shape[0]):
		print(grid[y][-1])

	for x in range(grid.shape[1] - 2, -1, -1):
		print(grid[-1][x])

	for y in range(grid.shape[0] - 2, 0, -1):
		print(grid[y][0])

	clockwise(grid[1:-1, 1:-1])


grid = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20]])
print(grid)
clockwise(grid)

grid = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
print(grid)
clockwise(grid)
