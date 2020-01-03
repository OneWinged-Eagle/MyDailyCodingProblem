"""
A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.
"""

import numpy as np
from typing import Tuple

possibleMoves = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2),
                 (-1, -2)]


def canGo(grid: np.ndarray, pos: Tuple[int, int]) -> bool:
	if 0 <= pos[0] < grid.shape[0] and 0 <= pos[1] < grid.shape[1] and not grid[
	    pos[0]][pos[1]]:
		return True

	return False


def helper(grid: np.ndarray,
           total: int,
           pos: Tuple[int, int] = (0, 0),
           visited: int = 1):
	if visited == total:
		return 1

	tours = 0

	for move in possibleMoves:
		newPos = (pos[0] + move[0], pos[1] + move[1])
		if canGo(grid, newPos):
			grid[newPos[0]][newPos[1]] = True
			tours += helper(grid, total, newPos, visited + 1)
			grid[newPos[0]][newPos[1]] = False

	return tours


def knightsTours(n: int) -> int:
	if n == 0:
		return 0

	grid = np.full((n, n), False)
	grid[0][0] = True

	return helper(grid, n * n)


for i in range(11):
	print(f"knightsTours({i}) = {knightsTours(i)}")
