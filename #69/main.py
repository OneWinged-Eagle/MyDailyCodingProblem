"""
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""

from math import inf
from typing import List


def productOfThree(numbers: List[int]) -> int:
	if len(numbers) < 3:
		return None

	min1, min2 = inf, inf
	max1, max2, max3 = -inf, -inf, -inf

	for nb in numbers:
		if nb < min1:
			min1, min2 = nb, min1
		elif nb < min2:
			min2 = nb

		if nb > max1:
			max1, max2, max3 = nb, max1, max2
		elif nb > max2:
			max2, max3 = nb, max2
		elif nb > max3:
			max3 = nb

	return max(min1 * min2 * max1, max1 * max2 * max3)


print(f"productOfThree([-10, -10, 5, 2]) = {productOfThree([-10, -10, 5, 2])}")
print(f"productOfThree([1, -10, 5, 2]) = {productOfThree([1, -10, 5, 2])}")
print(
    f"productOfThree([-10, -10, 5, 2, 40]) = {productOfThree([-10, -10, 5, 2, 40])}"
)
