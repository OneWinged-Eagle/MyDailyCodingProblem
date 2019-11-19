"""
You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]

Return two, as there are only two ways to get to the bottom right:

    Right, down, down, right
    Down, right, down, right

The top left corner and bottom right corner will always be 0.
"""

import numpy as np


def helper(board: np.ndarray, y: int = 0, x: int = 0) -> int:
	if y >= board.shape[0] or x >= board.shape[1] or board[y][x]:
		return 0

	if y == board.shape[0] - 1 and x == board.shape[1] - 1:
		return 1

	return helper(board, y + 1, x) + helper(board, y, x + 1)


def nbWays(board: np.ndarray) -> int:
	if len(board.shape) != 2 or board.shape[0] != board.shape[1] or board[0][
	    0] or board[-1][-1]:
		return None

	return helper(board)


board = np.array([[False, False, True], [False, False, True],
                  [True, False, False]])
assert nbWays(board) == 2
board[1][0] = True
assert nbWays(board) == 1
board[1][1] = True
assert nbWays(board) == 0
print("passed")
