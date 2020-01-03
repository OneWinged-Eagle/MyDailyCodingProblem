"""
Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""

from typing import List


def toLast(hops: List[int]) -> bool:
	if len(hops) <= 1:
		return True

	i, visited = 0, set()
	while i < len(hops) - 1:
		visited.add(i)

		i += hops[i]

		if i in visited:
			return False

	if i == len(hops) - 1:
		return True

	return False


print(f"toLast([2, 0, 1, 0]) = {toLast([2, 0, 1, 0])}")
print(f"toLast([1, 1, 0, 1]) = {toLast([1, 1, 0, 1])}")
print(f"toLast([2, 2, -1, 42]) = {toLast([2, 2, -1, 42])}")
print(f"toLast([2, 2, -2, 42]) = {toLast([2, 2, -2, 42])}")
print(f"toLast([2, 3, -1, 42]) = {toLast([2, 3, -1, 42])}")
