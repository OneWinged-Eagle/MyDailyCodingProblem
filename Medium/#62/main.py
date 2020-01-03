"""
There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

    Right, then down
    Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""

import numpy as np
from typing import NamedTuple


class Point(NamedTuple):
	x: int
	y: int


def nbWaysRec(n: int, m: int, start: Point = Point(0, 0)) -> int:
	if n - 1 == start.y and m - 1 == start.x:
		return 1

	ways = 0

	if start.x + 1 < m:
		ways += nbWaysRec(n, m, Point(start.x + 1, start.y))

	if start.y + 1 < n:
		ways += nbWaysRec(n, m, Point(start.x, start.y + 1))

	return ways


def nbWays(n: int, m: int) -> int:
	grid = np.ones((n, m), dtype=int)

	for x in range(1, m):
		for y in range(1, n):
			grid[y][x] = grid[y - 1][x] + grid[y][x - 1]

	return grid[n - 1][m - 1]


for n in range(1, 11):
	for m in range(1, 11):
		print(f"nbWays({n}, {m}) = {nbWays(n, m)}")
