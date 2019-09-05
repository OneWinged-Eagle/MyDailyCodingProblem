"""
Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
"""

from typing import List


def nonDecreasing(numbers: List[int]) -> bool:
	count = 0

	for i in range(len(numbers) - 1):
		if numbers[i] > numbers[i + 1]:
			count += 1

	return count <= 1


print(f"nonDecreasing([10, 5, 7]) = {nonDecreasing([10, 5, 7])}")
print(f"nonDecreasing([10, 5, 1]) = {nonDecreasing([10, 5, 1])}")
print(f"nonDecreasing([1, 10, 5, 7]) = {nonDecreasing([1, 10, 5, 7])}")
