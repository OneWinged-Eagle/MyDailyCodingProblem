"""
Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""

from functools import reduce
from typing import List, Tuple


def twoOnlyOnce(numbers: List[int]) -> Tuple[int, int]:
	if len(numbers) == 0:
		return None

	xor = reduce(lambda nb1, nb2: nb1 ^ nb2, numbers)
	bit = xor & ~(xor - 1)
	a, b = 0, 0

	for nb in numbers:
		if nb & bit:
			a = a ^ nb
		else:
			b = b ^ nb

	return a, b


assert twoOnlyOnce([2, 4, 6, 8, 10, 2, 6, 10]) == (4, 8)
print("passed")
