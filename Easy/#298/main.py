"""
A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion of her path that consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.
"""

from typing import List


def lengthOfTwo(array: List[int]) -> int:
	if len(array) <= 2:
		return len(array)

	first, second = 0, 1
	currLen = maxLen = 2

	for i in range(2, len(array)):
		if array[i] == array[first]:
			first, second = second, i
		elif array[i] != array[second]:
			first, second = second, i
			currLen, maxLen = i - first, max(maxLen, currLen)

		currLen += 1

	return maxLen


assert lengthOfTwo([2, 1, 2, 3, 3, 1, 3, 5]) == 4

print("passed")
