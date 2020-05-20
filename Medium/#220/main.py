"""
In front of you is a row of N coins, with values v1, v1, ..., vn.

You are asked to play the following game. You and an opponent take turns choosing either the first or last coin from the row, removing it from the row, and receiving the value of the coin.

Write a program that returns the maximum amount of money you can win with certainty, if you move first, assuming your opponent plays optimally.
"""

from typing import List


def maxMoney(values: List[int], curr: int = 0, me: bool = True) -> int:
	if len(values) == 0:
		return curr

	if me:
		return max(
		    maxMoney(values[1:], curr + values[0], False),
		    maxMoney(values[:-1], curr + values[-1], False))

	if values[0] > values[-1]:
		return maxMoney(values[1:], curr, True)

	return maxMoney(values[:-1], curr, True)


assert maxMoney([9, 4, 5, 7, 6, 10, 2, 5]) == 30
print('passed')
