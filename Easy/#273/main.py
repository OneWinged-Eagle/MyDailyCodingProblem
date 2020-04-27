"""
A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.
"""

from typing import List


def fixedPoint(array: List[int]) -> int:
	start, end = 0, len(array) - 1

	while start < end:
		half = (start + end) // 2

		if array[half] < half:
			start = half
		elif array[half] > half:
			end = half
		else:
			return half

	return -1


assert fixedPoint([-6, 0, 2, 40]) == 2
assert fixedPoint([-6, -5, 0, 3, 40]) == 3
assert fixedPoint([1, 5, 7, 8]) == -1
print('passed')
