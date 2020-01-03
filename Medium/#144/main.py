"""
Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""

from typing import List


def nearestLarger(numbers: List[int], i: int) -> int:
	left, right = i - 1, i + 1

	while ((left >= 0 and numbers[left] <= numbers[i]) or
	       (right < len(numbers) and numbers[right] <= numbers[i])) and not (
	           (left >= 0 and numbers[left] > numbers[i]) or
	           (right < len(numbers) and numbers[right] > numbers[i])):

		left -= 1
		right += 1

	if left >= 0 and numbers[left] > numbers[i]:
		return left
	elif right < len(numbers) and numbers[right] > numbers[i]:
		return right

	return None


nb = [4, 1, 3, 5, 6]
assert nearestLarger(nb, 0) == 3
assert nearestLarger(nb, 1) == 0
assert nearestLarger(nb, 2) == 3
assert nearestLarger(nb, 3) == 4
assert nearestLarger(nb, 4) == None
print(f"passed every indexes of {nb}")
