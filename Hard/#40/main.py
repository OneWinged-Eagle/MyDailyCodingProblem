"""
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""

from typing import List

# with n = len(numbers), Time O(n), Space O(n)
def bruteForce(numbers: List[int]) -> int:
	return (3 * sum(set(numbers)) - sum(numbers)) / 2

INT_SIZE = 32

# with n = len(numbers), Time O(n), Space O(1), but maybe a bit inefficient? (list to string to int)
def occursOnce(numbers: List[int]) -> int:
	bits = [0] * INT_SIZE

	for i in range(INT_SIZE):
		b = INT_SIZE - 1 - i
		for nb in numbers:
			if nb & (1 << i):
				bits[b] += 1
		bits[b] %= 3

	return int(''.join([str(bit) for bit in bits]), 2)

print(
    f"occursOnce([6, 1, 3, 3, 3, 6, 6]) = {occursOnce([6, 1, 3, 3, 3, 6, 6])}")
print(f"occursOnce([13, 19, 13, 13]) = {occursOnce([13, 19, 13, 13])}")
