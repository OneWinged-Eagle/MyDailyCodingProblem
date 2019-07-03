"""
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
"""

import numpy as np
from math import inf
from typing import NamedTuple


class MinCostArgs(NamedTuple):
	NK: str
	last: int


def minCost(NK: np.ndarray, last: int = -1) -> int:
	minCostArgs = MinCostArgs(repr(NK), last)

	if NK.size == 0:
		return 0
	elif minCostArgs in minCost.cache:
		print("Passing through...")
		return minCost.cache[minCostArgs]

	print("Not yet cached...")

	costs = [0] * NK.shape[1]

	for i, e in enumerate(NK[0]):
		if i == last:
			costs[i] = inf
		costs[i] += e + minCost(NK[1:], i)

	cost = min(costs)
	minCost.cache[minCostArgs] = cost
	return cost


minCost.cache = {}

print(
    f"minCost(np.array([[1, 2, 3, 4], [1, 2, 1, 0], [6, 1, 1, 5], [2, 3, 5, 5]])) = {minCost(np.array([[1, 2, 3, 4], [1, 2, 1, 0], [6, 1, 1, 5], [2, 3, 5, 5]]))}"
)

print(
    f"minCost(np.array([[1, 2, 4, 3], [1, 2, 4, 3], [3, 1, 2, 4], [3, 2, 1, 4]])) = {minCost(np.array([[1, 2, 4, 3], [1, 2, 4, 3], [3, 1, 2, 4], [3, 2, 1, 4]]))}"
)
print(
    f"minCost(np.array([[1, 2, 4, 3], [1, 2, 4, 3], [3, 1, 2, 4], [3, 2, 1, 4]])) = {minCost(np.array([[1, 2, 4, 3], [1, 2, 4, 3], [3, 1, 2, 4], [3, 2, 1, 4]]))}"
)  # test cache
print(minCost.cache)
