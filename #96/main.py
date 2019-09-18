"""
Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""

from typing import Any, List


def permutations(arr: List[Any]) -> List[List[Any]]:
	if not arr:
		return [[]]

	perm = []

	for i, elem in enumerate(arr):
		for p in permutations(arr[:i] + arr[i + 1:]):
			perm.append([elem] + p)

	return perm


print(f"permutations([1, 2, 3]) = {permutations([1, 2, 3])}")
