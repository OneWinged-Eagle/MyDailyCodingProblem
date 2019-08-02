"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""

from typing import List


def maxContiguousSum(numbers: List[int]) -> int:
	if not numbers:
		return 0

	currMax, maxSum = numbers[0], max(0, numbers[0])
	for nb in numbers[1:]:
		currMax = max(nb, currMax + nb)
		maxSum = max(currMax, maxSum)

	return maxSum


print(
    f"maxContiguousSum([34, -50, 42, 14, -5, 86]) = {maxContiguousSum([34, -50, 42, 14, -5, 86])}"
)
print(
    f"maxContiguousSum([-34, -50, 42, -14, -5, 86]) = {maxContiguousSum([-34, -50, 42, -14, -5, 86])}"
)
print(
    f"maxContiguousSum([-34, -50, 42, -14, -5, -86]) = {maxContiguousSum([-34, -50, 42, -14, -5, -86])}"
)
print(
    f"maxContiguousSum([-34, -50, -42, -14, -5, -86]) = {maxContiguousSum([-34, -50, -42, -14, -5, -86])}"
)
print(f"maxContiguousSum([42, 4]) = {maxContiguousSum([42, 4])}")
print(f"maxContiguousSum([42, -4]) = {maxContiguousSum([42, -4])}")
print(f"maxContiguousSum([-42, 4]) = {maxContiguousSum([-42, 4])}")
print(f"maxContiguousSum([-42, -4]) = {maxContiguousSum([-42, -4])}")
print(f"maxContiguousSum([42]) = {maxContiguousSum([42])}")
print(f"maxContiguousSum([-42]) = {maxContiguousSum([-42])}")
print(f"maxContiguousSum([]) = {maxContiguousSum([])}")
