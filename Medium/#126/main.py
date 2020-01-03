"""
Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. Try solving this without creating a copy of the list. How many swap or move operations do you need?
"""

from typing import Any, List


def reverse(arr: List[Any], start: int, end: int) -> List[Any]:
	for i in range((end - start) // 2):
		arr[start + i], arr[end - 1 - i] = arr[end - 1 - i], arr[start + i]

	return arr


def rotate(arr: List[Any], k: int) -> List[Any]:
	if k < 0:
		return None

	k %= len(arr)

	if k == 0:
		return arr

	arr.reverse()
	reverse(arr, 0, k)

	return reverse(arr, k, len(arr))


for n in range(13):
	print(f"rotate([1, 2, 3, 4, 5, 6], {n}) = {rotate([1, 2, 3, 4, 5, 6], n)}")
