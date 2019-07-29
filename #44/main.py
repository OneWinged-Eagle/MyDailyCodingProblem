"""
We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
"""

from typing import Any, List


# with n = len(arr), Time O(n²), Space O(1)
def bruteForce(arr: List[Any]) -> int:
	inversions = 0
	for i, nb1 in enumerate(arr):
		for nb2 in arr[i:]:
			if nb1 > nb2:
				inversions += 1
	return inversions


# with n = len(arr), Time O(n * log(n)), Space O(?) and arr changed in place
def outOfOrder(arr: List[Any]) -> int:
	if len(arr) == 1:
		return 0

	left, right = arr[:len(arr) // 2], arr[len(arr) // 2:]
	inversions = outOfOrder(left) + outOfOrder(right)
	l, r = 0, 0

	while l < len(left) and r < len(right):
		if left[l] < right[r]:
			arr[l + r] = left[l]
			l += 1
		else:
			inversions += len(left) - l
			arr[l + r] = right[r]
			r += 1

	if l != r:
		arr[l + r] = left[l] if l < len(left) else right[r]

	return inversions


print(f"[2, 4, 1, 3, 5] = {outOfOrder([2, 4, 1, 3, 5])}")
print(f"[5, 4, 3, 2, 1] = {outOfOrder([5, 4, 3, 2, 1])}")
