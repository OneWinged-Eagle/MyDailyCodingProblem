"""
Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
"""

import numpy as np


def crossed(grid: np.ndarray, target: str) -> bool:
	for y in range(grid.shape[0]):
		if target in ''.join(grid[y]):
			return True

	for x in range(grid.shape[1]):
		if target in ''.join(grid[:, x]):
			return True

	return False


grid = np.array([['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'],
                 ['A', 'N', 'O', 'B'], ['M', 'A', 'S', 'S']])

print(grid)
print(f"crossed(grid, 'FOAM') = {crossed(grid, 'FOAM')}")
print(f"crossed(grid, 'FOAA') = {crossed(grid, 'FOAA')}")
print(f"crossed(grid, 'MASS') = {crossed(grid, 'MASS')}")
print(f"crossed(grid, 'MASB') = {crossed(grid, 'MASB')}")
print(f"crossed(grid, 'NOB') = {crossed(grid, 'NOB')}")
print(f"crossed(grid, 'NOS') = {crossed(grid, 'NOS')}")
print(f"crossed(grid, 'OS') = {crossed(grid, 'OS')}")
print(f"crossed(grid, 'QB') = {crossed(grid, 'QB')}")
