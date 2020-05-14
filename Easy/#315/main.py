"""
In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.

Here is an example:

1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2

Write a program to determine whether a given input is a Toeplitz matrix.
"""

from typing import Any, List


def isMatrix(matrix: List[List[Any]]) -> bool:
	if len(matrix) == 0:
		return False

	return all([len(matrix[0]) == len(x) for x in matrix])


def isToeplitz(matrix: List[List[Any]]) -> bool:
	if len(matrix) == 1:
		return True

	if not isMatrix(matrix):
		return False

	m = 1

	while m < len(matrix):
		for i, n in enumerate(matrix[m]):
			if (i > 0 and n != matrix[m - 1][i - 1]) or (m + 1 < len(matrix) and
			                                             i + 1 < len(matrix[m]) and
			                                             n != matrix[m + 1][i + 1]):
				return False

		m = min(m + 3, len(matrix))

	return True


assert not isToeplitz([])
assert isToeplitz([[1]])
assert isToeplitz([[1, 2]])
assert not isToeplitz([[1, 2], [3, 4]])
assert isToeplitz([[1, 2], [3, 1]])
assert isToeplitz([[1, 2, 3, 4, 8], [5, 1, 2, 3, 4], [4, 5, 1, 2, 3],
                   [7, 4, 5, 1, 2]])
assert not isToeplitz([[1, 2, 3, 4, 8], [5, 1, 2, 3, 4], [4, 5, 10, 2, 3],
                       [7, 4, 5, 1, 2]])
assert isToeplitz([[1, 2, 3, 4, 8], [5, 1, 2, 3, 4], [4, 5, 1, 2, 3]])
assert not isToeplitz([[1, 2, 3, 4, 8], [5, 1, 2, 3, 4], [4, 5, 10, 2, 3]])
assert isToeplitz([[1, 2, 3, 4, 8], [5, 1, 2, 3, 4]])
assert not isToeplitz([[1, 2, 3, 4, 8], [5, 10, 2, 3, 4]])

print('passed')
