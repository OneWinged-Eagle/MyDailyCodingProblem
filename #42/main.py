"""
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
			helper.cache[helperArgs] = tmp + [numbers[-1]] if tmp != None else helper(
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
