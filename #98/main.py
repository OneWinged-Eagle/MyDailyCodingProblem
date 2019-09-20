"""
Given a 2D board of characters and a word, find if the word exists in the board.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
"""

import numpy as np


def helper(board: np.ndarray, word: str, y: int, x: int) -> bool:
	if not word or len(word) == 0:
		return True

	if y < 0 or y >= board.shape[0] or x < 0 or x >= board.shape[1] or word[
	    0] != board[y][x]:
		return False

	board[y][x] = None
	return helper(board, word[1:], y - 1, x) or helper(
	    board, word[1:], y, x + 1) or helper(board, word[1:], y + 1, x) or helper(
	        board, word[1:], y, x - 1)


def exists(board: np.ndarray, word: str) -> bool:
	for (y, x), _ in np.ndenumerate(board):
		if helper(np.copy(board), word, y, x):
			return True

	return False


board = np.array([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'],
                  ['A', 'D', 'E', 'E']])
print(f"board = {board}")
print(f"exists(board, 'ABCCED') = {exists(board, 'ABCCED')}")
print(f"exists(board, 'SEE') = {exists(board, 'SEE')}")
print(f"exists(board, 'ABCB') = {exists(board, 'ABCB')}")
print(f"exists(board, 'ABCESCF') = {exists(board, 'ABCESCF')}")
print(f"exists(board, 'ABCESCFB') = {exists(board, 'ABCESCFB')}")
print(f"exists(board, 'ABCESCFSA') = {exists(board, 'ABCESCFSA')}")
