"""
You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi

This is not ordered because of the a in the center. We can remove the second column to make it ordered:

ca
df
gi

So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef

Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

zyx
wvu
tsr

Your function should return 3, since we would need to remove all the columns to order it.
"""

import numpy as np


# time O(n), space O(1)
def rmColumns(grid: np.ndarray) -> int:
	if grid.shape[0] <= 1 or grid.shape[1] == 0:
		return 0

	nbColumns = 0

	for column in grid.T:
		if not all(column[i] <= column[i + 1] for i in range(len(column) - 1)):
			nbColumns += 1

	return nbColumns


grid = np.array([['c', 'b', 'a'], ['d', 'a', 'f'], ['g', 'h', 'i']])
print(f"rmColumns({grid}) = {rmColumns(grid)}")

grid = np.array([['a', 'b', 'c', 'd', 'e', 'f']])
print(f"rmColumns({grid}) = {rmColumns(grid)}")

grid = np.array([['z', 'y', 'x'], ['w', 'v', 'u'], ['t', 's', 'r']])
print(f"rmColumns({grid}) = {rmColumns(grid)}")
