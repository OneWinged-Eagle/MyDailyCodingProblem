"""
Given an array of integers, determine whether it contains a Pythagorean triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.
"""

from typing import List


def pythagorean(array: List[int]) -> bool:
	squares = set([x**2 for x in array])
	print(squares)

	for n in squares:
		s = set([x - n for x in squares])
		if any([x in squares for x in s]):
			return True

	return False


assert pythagorean([3, 4, 5])
assert pythagorean([3, 1, 9, 6, 2, 7, 10, 4, 8])
assert pythagorean([3, 1, 9, 6, 2, 7, 10, 4, 5])
assert not pythagorean([3, 1, 9, 6, 2, 7, 10, 4])

print("passed")
