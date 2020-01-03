"""
Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.
"""

from math import inf
from typing import List, Tuple


def smallestInterval(intervals: List[Tuple[int, int]]) -> Tuple[int, int]:
	if intervals is None or len(intervals) == 0:
		return None

	smallestMax, biggestMin = inf, -inf

	for interval in intervals:
		mi, ma = min(interval), max(interval)

		if mi > biggestMin:
			biggestMin = mi

		if ma < smallestMax:
			smallestMax = ma

	return smallestMax, biggestMin


print(
    f"smallestInterval([(0, 3), (2, 6), (3, 4), (6, 9)]) = {smallestInterval([(0, 3), (2, 6), (3, 4), (6, 9)])}"
)
print(
    f"smallestInterval([(0, 3), (2, 6), (3, 4), (6, 9), (-10, 10)]) = {smallestInterval([(0, 3), (2, 6), (3, 4), (6, 9), (-10, 10)])}"
)
print(f"smallestInterval([]) = {smallestInterval([])}")
