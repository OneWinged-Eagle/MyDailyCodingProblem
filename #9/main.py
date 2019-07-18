"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def maxSumNonAdjacent(numbers):
	if not numbers:
		return None
	elif len(numbers) == 1:
		return numbers[0]

	maxSumWithPrev, maxSumWithoutPrev = numbers[1], numbers[0]

	for nb in numbers[2:]:
		maxSumWithPrev, maxSumWithoutPrev = maxSumWithoutPrev + nb, max(
		    maxSumWithPrev, maxSumWithoutPrev)

	return max(maxSumWithPrev, maxSumWithoutPrev)


print(
    f"maxSumNonAdjacent([2, 4, 6, 2, 5]) = {maxSumNonAdjacent([2, 4, 6, 2, 5])}"
)

print(
    f"maxSumNonAdjacent([-2, -4, -6, -2, -5]) = {maxSumNonAdjacent([-2, -4, -6, -2, -5])}"
)

print(
    f"maxSumNonAdjacent([2, 4, -6, 2, 5]) = {maxSumNonAdjacent([2, 4, -6, 2, 5])}"
)

print(f"maxSumNonAdjacent([5, 1, 1, 5]) = {maxSumNonAdjacent([5, 1, 1, 5])}")

print(
    f"maxSumNonAdjacent([-5, -1, -1, -5]) = {maxSumNonAdjacent([-5, -1, -1, -5])}"
)

print(
    f"maxSumNonAdjacent([-5, 1, -1, 5]) = {maxSumNonAdjacent([-5, 1, -1, 5])}")
