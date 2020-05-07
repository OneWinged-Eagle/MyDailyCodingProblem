"""
Given an unsorted array, in which all elements are distinct, find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both its left and right neighbors. It is guaranteed that the first and last elements are lower than all others.
"""

from typing import List


def peak(array: List[int]) -> int:
	if len(array) == 0:
		return -1

	if len(array) == 1:
		return array[0]

	half = len(array) // 2

	if array[half - 1] < array[half] > array[half + 1]:
		return half

	if array[half - 1] > array[half]:
		return peak(array[:half + 1])

	return peak(array[half:])


assert peak([10, 20, 25, 30, 15, 5]) == 3
assert peak([1, 8, 2, 3, 4, 0]) == 1
print("passed")
