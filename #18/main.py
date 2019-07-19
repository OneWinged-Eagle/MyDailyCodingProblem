"""
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
"""

from collections import deque
from typing import List


# with n = len(numbers), time O(n * k), space O(n)
def bruteForce(numbers: List[int], k: int) -> List[int]:
	maxSubarrays = []

	for i in range(0, len(numbers) + 1 - k):
		maxSubarrays.append(max(numbers[i:i + k]))

	return maxSubarrays


# with n = len(numbers), time O(n), space O(n) (can become O(k) if print in place of maxSubarrays))
def maxSubarrays(numbers: List[int], k: int) -> List[int]:
	if k < 1 or k > len(numbers):
		return None

	queue = deque()
	maxSubarrays = []

	for i in range(len(numbers)):
		while queue and queue[0] <= i - k:
			queue.popleft()

		while queue and numbers[i] >= numbers[queue[-1]]:
			queue.pop()

		queue.append(i)
		if i >= k - 1:
			maxSubarrays.append(numbers[queue[0]])

	return maxSubarrays


print(
    f"maxSubarrays([10, 5, 2, 7, 8, 7], 0) = {maxSubarrays([10, 5, 2, 7, 8, 7], 0)}"
)
print(
    f"maxSubarrays([10, 5, 2, 7, 8, 7], 1) = {maxSubarrays([10, 5, 2, 7, 8, 7], 1)}"
)
print(
    f"maxSubarrays([10, 5, 2, 7, 8, 7], 2) = {maxSubarrays([10, 5, 2, 7, 8, 7], 2)}"
)
print(
    f"maxSubarrays([10, 5, 2, 7, 8, 7], 3) = {maxSubarrays([10, 5, 2, 7, 8, 7], 3)}"
)
print(
    f"maxSubarrays([10, 5, 2, 7, 8, 7], 4) = {maxSubarrays([10, 5, 2, 7, 8, 7], 4)}"
)
print(
    f"maxSubarrays([10, 5, 2, 7, 8, 7], 5) = {maxSubarrays([10, 5, 2, 7, 8, 7], 5)}"
)
print(
    f"maxSubarrays([10, 5, 2, 7, 8, 7], 6) = {maxSubarrays([10, 5, 2, 7, 8, 7], 6)}"
)
print(
    f"maxSubarrays([10, 5, 2, 7, 8, 7], 7) = {maxSubarrays([10, 5, 2, 7, 8, 7], 7)}"
)
