"""
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.
"""

import numpy as np
from typing import List


def partitioned(numbers: List[int]) -> bool:
	total = sum(numbers)
	if total % 2 != 0:
		return False

	canSumTable = np.full((total // 2 + 1, len(numbers) + 1), False)
	canSumTable[0] = True

	for y in range(1, total // 2 + 1):
		for x in range(1, len(numbers) + 1):
			canSumTable[y][x] = canSumTable[y - 1][x]

			if not canSumTable[y][x] and y >= numbers[x - 1]:
				canSumTable[y][x] = canSumTable[y - numbers[x - 1]][x - 1]

	return canSumTable[total // 2][len(numbers)]


print(
    f"partitioned([15, 5, 20, 10, 35, 15, 10]) = {partitioned([15, 5, 20, 10, 35, 15, 10])}"
)
print(f"partitioned([15, 5, 20, 10, 35]) = {partitioned([15, 5, 20, 10, 35])}")
print(
    f"partitioned([2, 1, 3, 4, 5, 4, 1]) = {partitioned([2, 1, 3, 4, 5, 4, 1])}"
)
