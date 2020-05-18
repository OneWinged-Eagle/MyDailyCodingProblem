"""
Given an array of numbers and a number k, determine if there are three entries in the array which add up to the specified number k. For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.
"""

from typing import List


def threeAddUpV1(array: List[int], k: int) -> bool:
	pluses = [[n + nn
	           for ii, nn in enumerate(array)
	           if i != ii]
	          for i, n in enumerate(array)]

	for plus in pluses:
		s = set(plus)

		for n in array:
			if (k - n) in s:
				return True

	return False


def threeAddUp(array: List[int], k: int) -> bool:
	array.sort()

	for i, n in enumerate(array):
		left, right = i + 1, len(array) - 1

		while left < right:
			s = array[left] + array[i] + array[right]

			if s < k:
				left += 1
			elif s > k:
				right -= 1
			else:
				return True

	return False


assert threeAddUp([20, 303, 3, 4, 25], 49)
print('passed')
