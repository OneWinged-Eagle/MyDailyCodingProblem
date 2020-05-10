"""
Given a positive integer N, find the smallest number of steps it will take to reach 1.

There are two kinds of permitted steps:

    You may decrement N to N - 1.
    If a * b = N, you may decrement N to the larger of a and b.

For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.
"""

from math import floor, sqrt
from queue import Queue


def steps(nb: int) -> int:
	queue = Queue()
	cache = set()

	queue.put((nb, 0))

	while not queue.empty():
		currNb, currSteps = queue.get()

		if currNb == 1:
			return currSteps

		if currNb - 1 not in cache:
			queue.put((currNb - 1, currSteps + 1))
			cache.add(currNb - 1)

		for i in range(2, floor(sqrt(currNb)) + 1):
			divisor = currNb // i

			if currNb % i == 0 and divisor not in cache:
				queue.put((divisor, currSteps + 1))
				cache.add(divisor)

	return -1


assert steps(100) == 5
print("passed")
