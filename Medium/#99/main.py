"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

from typing import List


def longest(numbers: List[int]) -> int:
	d = dict()
	l = 0

	for nb in numbers:
		if nb not in d:
			if nb + 1 in d and nb - 1 in d:
				top, le1 = d[nb + 1]
				bottom, le2 = d[nb - 1]

				del d[nb + 1]
				del d[nb - 1]

				d[top] = (bottom, le1 + le2 + 1)
				d[bottom] = (top, le1 + le2 + 1)

				l = max(l, le1 + le2 + 1)

			elif nb + 1 in d:
				top, le = d[nb + 1]

				del d[nb + 1]

				d[top] = (nb, le + 1)
				d[nb] = (top, le + 1)

				l = max(l, le + 1)

			elif nb - 1 in d:
				bottom, le = d[nb - 1]

				del d[nb - 1]

				d[bottom] = (nb, le + 1)
				d[nb] = (bottom, le + 1)

				l = max(l, le + 1)

			else:
				d[nb] = (nb, 1)

	return l


print(f"longest([100, 4, 200, 1, 3, 2]) = {longest([100, 4, 200, 1, 3, 2])}")
