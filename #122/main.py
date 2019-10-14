"""
You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1

The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
"""

import numpy as np


def maxCoinsRec(grid: np.ndarray, y: int = 0, x: int = 0) -> int:
	if grid is None or y < 0 or y >= grid.shape[0] or x < 0 or x >= grid.shape[1]:
		return 0

	return grid[y][x] + max(
	    maxCoinsRec(grid, y + 1, x), maxCoinsRec(grid, y, x + 1))


def maxCoins(grid: np.ndarray) -> int:
	if grid is None:
		return None

	cost = grid.copy()
	for y in range(1, grid.shape[0]):
		cost[y][0] += cost[y - 1][0]

	for x in range(1, grid.shape[1]):
		cost[0][x] += cost[0][x - 1]

	for y in range(1, grid.shape[0]):
		for x in range(1, grid.shape[1]):
			cost[y][x] += max(cost[y - 1][x], cost[y][x - 1])

	return cost[-1][-1]


grid = np.array([[0, 3, 1, 1], [2, 0, 0, 4], [1, 5, 3, 1]])
print(f"maxCoins({grid}) = {maxCoins(grid)}")

grid = np.array([[0, 3, 1, 1], [2, 5, 6, 4], [1, 5, 3, 1]])
print(f"maxCoins({grid}) = {maxCoins(grid)}")
