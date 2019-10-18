"""
Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""

from typing import List


def helper(numbers: List[int], K: int, total: int) -> List[int]:
	if not numbers or len(numbers) == 0:
		return None

	if total == K:
		return numbers

	left = helper(numbers[:-1], K, total - numbers[-1])
	if left is not None:
		return left
	return helper(numbers[1:], K, total - numbers[0])


def sumToRec(numbers: List[int], K: int) -> List[int]:
	if not numbers or len(numbers) == 0:
		return None

	return helper(numbers, K, sum(numbers))


def sumTo(numbers: List[int], K: int) -> List[int]:
	if not numbers or len(numbers) == 0:
		return None

	sums = dict()
	currSum = 0

	for i in range(len(numbers)):
		currSum += numbers[i]

		if currSum == K:
			return numbers[:i + 1]

		if currSum - K in sums:
			return numbers[sums[currSum - K] + 1:i + 1]

		sums[currSum] = i

	return None


print(f"sumTo([1, 2, 3, 4, 5], 9) = {sumTo([1, 2, 3, 4, 5], 9)}")
print(f"sumTo([-10, -20, 5, 2, -14], -27) = {sumTo([-10, -20, 5, 2, -14], -27)}")
print(f"sumTo([], 9) = {sumTo([], 9)}")
print(f"sumTo([10, -15, 5, 25, -10], 20) = {sumTo([10, -15, 5, 25, -10], 20)}")
print(f"sumTo([10, -15, 5, 25, -10], 0) = {sumTo([10, -15, 5, 25, -10], 0)}")
print(f"sumTo([10, -15, 5, 25, -10], 42) = {sumTo([10, -15, 5, 25, -10], 42)}")
