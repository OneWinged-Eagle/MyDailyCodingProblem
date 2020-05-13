"""
The 24 game is played as follows. You are given a list of four integers, each between 1 and 9, in a fixed order. By placing the operators +, -, *, and / between the numbers, and grouping them with parentheses, determine whether it is possible to reach the value 24.

For example, given the input [5, 2, 7, 8], you should return True, since (5 * 2 - 7) * 8 = 24.

Write a function that plays the 24 game.
"""

from typing import List


def game(digits: List[int], target: int) -> bool:
	if len(digits) == 0:
		return False

	if len(digits) == 1:
		return digits[0] == target

	calculus = list()
	for i in range(len(digits) - 1):
		nb1, nb2 = digits[i], digits[i + 1]

		calculus.append(digits[:i] + [nb1 + nb2] + digits[i + 2:])

		calculus.append(digits[:i] + [nb1 - nb2] + digits[i + 2:])

		calculus.append(digits[:i] + [nb1 * nb2] + digits[i + 2:])

		if nb2 != 0:
			calculus.append(digits[:i] + [nb1 // nb2] + digits[i + 2:])

	return any(game(c, target) for c in calculus)


assert game([5, 2, 7, 8], 24)
assert game([42, 77, 69, 4], 40)
print('passed')
