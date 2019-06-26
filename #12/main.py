"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

from typing import List, NamedTuple


class NbWaysArgs(NamedTuple):
	N: int
	X: str


def nbWays(N: int, X: List[int]) -> int:
	nbWaysArgs = NbWaysArgs(N, repr(X))

	if N < 0:
		return 0
	elif N == 0:
		return 1
	elif nbWaysArgs in nbWays.cache:
		print("Passing through...")
		return nbWays.cache[nbWaysArgs]

	ways = 0

	for x in X:
		ways += nbWays(N - x, X)

	nbWays.cache[nbWaysArgs] = ways

	return ways


nbWays.cache = {}

print(f"nbWays(4, [1, 2] = {nbWays(4, [1, 2])}")
print(f"nbWays(5, [1, 2, 3]) = {nbWays(5, [1, 2, 3])}")
print(f"nbWays(6, [1, 2, 3, 5]) = {nbWays(6, [1, 2, 3, 5])}")
print(f"nbWays(6, [1, 2, 3, 5]) = {nbWays(6, [1, 2, 3, 5])}") # test cache
print(nbWays.cache)
