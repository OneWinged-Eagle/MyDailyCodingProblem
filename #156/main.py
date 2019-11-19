"""
Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3² + 2² = 9 + 4.

Given n = 27, return 3 since 27 = 3² + 3² + 3² = 9 + 9 + 9.
"""

from math import sqrt

squares = [0, 1, 2, 3]


def nextSquare() -> int:
	square = n = len(squares)

	for i in range(1, int(sqrt(n)) + 1):
		tmp = i * i

		if tmp > n:
			break
		else:
			square = min(square, 1 + squares[n - tmp])

	return square


def nbSquaredTo(n: int) -> int:
	if n < 0:
		return None

	while len(squares) <= n:
		squares.append(nextSquare())

	return squares[n]


for n in range(21):
	print(f"nbSquaredTo({n}) = {nbSquaredTo(n)}")
