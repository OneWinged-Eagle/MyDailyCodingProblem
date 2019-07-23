"""
Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

    Any live cell with less than two live neighbours dies.
    Any live cell with two or three live neighbours remains living.
    Any live cell with more than three live neighbours dies.
    Any dead cell with exactly three live neighbours becomes a live cell.

A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""

from itertools import product
from math import inf
import numpy as np
from typing import NamedTuple, Set


class Pos(NamedTuple):
	x: int
	y: int


class GameOfLife:
	grid: np.ndarray
	width: int
	height: int

	def __init__(self, cellsPos: Set[Pos], steps: int):
		minPos = Pos(inf, inf)
		maxPos = Pos(-inf, -inf)
		for pos in cellsPos:
			if pos.x < minPos.x:
				minPos = minPos._replace(x=pos.x)
			if pos.x > maxPos.x:
				maxPos = maxPos._replace(x=pos.x)

			if pos.y < minPos.y:
				minPos = minPos._replace(y=pos.y)
			if pos.y > maxPos.y:
				maxPos = maxPos._replace(y=pos.y)

		self.width = maxPos.x - minPos.x + 3
		self.height = maxPos.y - minPos.y + 3
		self.grid = np.full((self.height, self.width), False)
		for pos in cellsPos:
			self.grid[pos.y + 1 - minPos.y, pos.x + 1 - minPos.x] = True

		self.run(steps)

	def getNeighbours(self, currY: int, currX: int) -> int:
		neighbours = 0

		for y, x in product(
		    range(currY - 1, currY + 2), range(currX - 1, currX + 2)):
			if (y == currY and
			    x == currX) or y < 0 or x < 0 or x >= self.width or y >= self.height:
				continue

			if self.grid[y, x]:
				neighbours += 1

		return neighbours

	def tick(self):
		newGrid = self.grid.copy()

		for (y, x), cell in np.ndenumerate(self.grid):
			neighbours = self.getNeighbours(y, x)

			if cell and (neighbours < 2 or neighbours > 3):
				newGrid[y, x] = False
			elif not cell and neighbours == 3:
				newGrid[y, x] = True

		if any(newGrid[0]):
			newGrid = np.append(np.full((1, self.width), False), newGrid, axis=0)
			self.height += 1
		if any(newGrid[:, 0]):
			newGrid = np.append(np.full((self.height, 1), False), newGrid, axis=1)
			self.width += 1
		if any(newGrid[-1]):
			newGrid = np.append(newGrid, np.full((1, self.width), False), axis=0)
			self.height += 1
		if any(newGrid[:, -1]):
			newGrid = np.append(newGrid, np.full((self.height, 1), False), axis=1)
			self.width += 1

		self.grid = newGrid

	def run(self, steps: int):
		print(f"Starting state:\n{self}\n")

		for i in range(steps):
			self.tick()
			print(f"After {i} steps:\n{self}\n")

	def __repr__(self):
		return '\n'.join(
		    ' '.join('*' if cell else '.' for cell in row) for row in self.grid)


glider = GameOfLife(
    {
        Pos(2, 0),
        Pos(2, 1),
        Pos(2, 2),
        Pos(1, 2),
        Pos(0, 1),
        Pos(15, 2),
        Pos(14, 3),
        Pos(15, 3),
        Pos(16, 3),
        Pos(2, 15),
        Pos(3, 14),
        Pos(3, 15),
        Pos(3, 16)
    }, 200)
