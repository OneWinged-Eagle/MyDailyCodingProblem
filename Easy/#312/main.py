"""
You are given a 2 x N board, and instructed to completely cover the board with the following shapes:

    Dominoes, or 2 x 1 rectangles.
    Trominoes, or L-shapes.

For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.

A B B C
A B C C

Given an integer N, determine in how many ways this task is possible.
"""


def ways(N: int) -> int:
	if N <= 0:
		return 0

	if N == 1:
		return 1

	if N == 2:
		return 2

	if N == 3:
		return 5

	return 2 * ways(N - 1) + ways(N - 3)


assert ways(1) == 1
assert ways(2) == 2
assert ways(3) == 5
assert ways(4) == 11
print('passed')
