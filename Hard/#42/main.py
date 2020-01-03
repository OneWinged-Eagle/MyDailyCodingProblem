"""
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""

from typing import List, NamedTuple


class HelperArgs(NamedTuple):
	numbers: str
	currSum: int


# not sure that the cache is really that useful
def helper(numbers: List[int], currSum: int, k: int) -> List[int]:
	helperArgs = HelperArgs(repr(numbers), currSum)

	if helperArgs not in helper.cache:
		if currSum == k:
			helper.cache[helperArgs] = numbers

		elif not numbers:
			helper.cache[helperArgs] = None

		else:
			tmp = helper(numbers[:-1], currSum, k)
			helper.cache[helperArgs] = tmp + [numbers[-1]] if tmp is not None else helper(
			    numbers[:-1], currSum - numbers[-1], k)

	return helper.cache[helperArgs]


def sumTo(numbers: List[int], k: int) -> List[int]:
	helper.cache = {}
	return helper(numbers, sum(numbers), k)


print(f"sumTo([12, 1, 61, 5, 9, 2], 24) = {sumTo([12, 1, 61, 5, 9, 2], 24)}")
print(f"sumTo([1, 7, 5, 8, 2], 22) = {sumTo([1, 7, 5, 8, 2], 22)}")
print(f"sumTo([1, 7, 5, 8, 2, -5], -2) = {sumTo([1, 7, 5, 8, 2, -5], -2)}")
print(
    f"sumTo([12, 1, 61, 5, 9, 2], 1000) = {sumTo([12, 1, 61, 5, 9, 2], 1000)}")
