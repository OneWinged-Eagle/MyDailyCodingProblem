"""
An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
"""

from typing import List


# with n = len(arr), Time O(log n), Space O(1)
def getIndex(arr: List[int], elem: int, offset: int = 0) -> int:
	if not arr:
		return -1

	if arr[0] == elem:
		return offset

	mid = len(arr) // 2
	if arr[mid] == elem:
		return offset + mid

	if arr[-1] == elem:
		return offset + len(arr) - 1

	if arr[0] < arr[mid]:
		if arr[0] < elem < arr[mid]:
			return getIndex(arr[:mid], elem, offset)

		return getIndex(arr[mid + 1:], elem, offset + mid + 1)

	if arr[mid] < elem < arr[-1]:
		return getIndex(arr[mid + 1:], elem, offset + mid + 1)

	return getIndex(arr[:mid], elem, offset)


arr = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for nb in arr:
	print(f"getIndex({arr}, {nb}) = {getIndex(arr, nb)}")

arr = [
    42, 43, 44, 45, 46, 47, 48, 49, 50, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
    40, 41
]
for nb in arr:
	print(f"getIndex({arr}, {nb}) = {getIndex(arr, nb)}")
