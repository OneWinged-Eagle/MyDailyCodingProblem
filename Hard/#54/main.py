"""
Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.
"""

import numpy as np


class Sudoku:
	grid: np.ndarray

	def __init__(self, grid: np.ndarray):
		self.grid = grid

	def canPut(self, x: int, y: int, nb: int) -> bool:
		xSquare, ySquare = x // 3 * 3, y // 3 * 3

		if nb in self.grid[:, x] or nb in self.grid[y] or nb in self.grid[
		    ySquare:ySquare + 3, xSquare:xSquare + 3]:
			return False

		return True

	def solve(self, x: int = 0, y: int = 0):
		if x > 8:
			x = 0
			y += 1

		if self.grid[y][x] != 0:
			return self.solve(x + 1, y)

		for n in range(1, 10):
			if (self.canPut(x, y, n)):
				self.grid[y][x] = n
				if y == 8 and x == 8:
					return True
				elif self.solve(x + 1, y):
					return True
				self.grid[y][x] = 0

		return False

	def __repr__(self):
		return '\n'.join(
		    '|'.join(repr(nb) if nb else ' ' for nb in row) for row in self.grid)


sudoku = Sudoku(
    np.array([[8, 6, 0, 0, 0, 3, 0, 0, 0], [0, 0, 0, 5, 0, 9, 1, 0, 2],
              [0, 0, 0, 0, 4, 0, 0, 0, 0], [2, 0, 6, 0, 0, 0, 3, 0, 5],
              [0, 0, 0, 0, 0, 0, 7, 0, 0], [0, 4, 0, 0, 0, 0, 0, 0, 1],
              [4, 3, 2, 0, 0, 0, 0, 0, 7], [0, 1, 0, 6, 0, 8, 0, 0, 0],
              [0, 0, 0, 0, 0, 2, 0, 0, 0]]))
print(f"sudoku = \n{sudoku}")
sudoku.solve()
print(f"sudoku = \n{sudoku}")
