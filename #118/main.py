"""
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""

from typing import List


def mergeSort(numbers: List[int], left: List[int],
              right: List[int]) -> List[int]:
	l, r = 0, 0

	while l + r < len(numbers):
		if r == len(right) or (l < len(left) and left[l] <= right[r]):
			numbers[l + r] = left[l]
			l += 1
		else:
			numbers[l + r] = right[r]
			r += 1

	return numbers


def square(numbers: List[int]) -> List[int]:
	if len(numbers) == 0 or any(
	    numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1)):
		return None

	index = -1

	for i, nb in enumerate(numbers):
		if index == -1 and nb >= 0:
			index = i

		numbers[i] = nb * nb

	if index == -1 or numbers[-1] == 0:
		numbers.reverse()
		index = 0

	return numbers if index == 0 else mergeSort(numbers, numbers[index - 1::-1],
	                                            numbers[index:])


print(
    f"square([-0, 0, 2, 2, 3, 9, 10, 42]) = {square([-0, 0, 2, 2, 3, 9, 10, 42])}"
)
print(
    f"square([-42, -9, -2, -0, 0, 2, 3, 10]) = {square([-42, -9, -2, -0, 0, 2, 3, 10])}"
)
print(
    f"square([-42, -10, -9, -3, -2, -2, -0, 0]) = {square([-42, -10, -9, -3, -2, -2, -0, 0])}"
)

print(f"square([-0, 2, 4, -6, -8, 10]) = {square([-0, 2, 4, -6, -8, 10])}")
print(f"square([]) = {square([])}")

print(f"square([2, 2, 3, 9, 10, 42]) = {square([2, 2, 3, 9, 10, 42])}")
print(f"square([-42, -9, -2, 2, 3, 10]) = {square([-42, -9, -2, 2, 3, 10])}")
print(
    f"square([-42, -10, -9, -3, -2, -2]) = {square([-42, -10, -9, -3, -2, -2])}"
)
