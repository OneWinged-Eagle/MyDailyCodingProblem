"""
A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.
"""

from typing import List


def helper(n: int, base: int) -> List[str]:
	if n == 0:
		return [""]

	if n == 1:
		return ["1", "0", "8"]

	middles = helper(n - 2, base)

	result = []

	for middle in middles:
		if n != base:
			result.append("0" + middle + "0")

		result.append("1" + middle + "1")
		result.append("6" + middle + "9")
		result.append("8" + middle + "8")
		result.append("9" + middle + "6")

	return result


def strobogrammatic(n: int) -> List[int]:
	if n == 0:
		return []

	return list(map(int, helper(n, n)))


for i in range(5):
	print(f"strobogrammatic({i}) = \{strobogrammatic(i)}/")
