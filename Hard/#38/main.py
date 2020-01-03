"""
You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.
"""

from typing import List


def queenAt(i: int, queensPos: List[int], n: int) -> bool:
	x, y = i % n, i // n
	if queensPos[y] == -1 and all(
	    pos == -1 or (pos != x and abs(pos - x) != abs(index - y))
	    for index, pos in enumerate(queensPos)):
		return True
	return False


def helper(queensPos: List[int], n: int, i: int = 0) -> int:
	if i >= n * n:
		if all(pos != -1 for pos in queensPos):
			return 1
		return 0

	x, y = i % n, i // n
	if y > 0 and queensPos[y - 1] == -1:
		return 0

	total = helper(queensPos, n, i + 1)

	if queenAt(i, queensPos, n):
		newPos = list(queensPos)
		newPos[y] = x
		total += helper(newPos, n, i + n - x)

	return total


# a bit slow, can surely improve by "caching" the queenAt function
# read about "symmetry breaking" too, can try that...
def queens(n: int) -> int:
	if n <= 0:
		return 0

	return helper([-1] * n, n)


for i in range(11):
	print(f"queens({i}) = {queens(i)}")
