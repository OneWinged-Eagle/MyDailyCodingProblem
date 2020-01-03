"""
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
"""

from random import shuffle
from typing import List, NamedTuple


class Interval(NamedTuple):
	start: int
	end: int

	def __repr__(self):
		return f"({self.start}, {self.end})"


# time O(n²), space O(1), in place
def mergeNCube(intervals: List[Interval]) -> List[Interval]:
	if not intervals or len(intervals) == 0:
		return intervals

	for i, intI in reversed(list(enumerate(intervals))):
		for j, intJ in enumerate(intervals[:i]):
			if intI.start <= intJ.end or intJ.start <= intI.end:
				intervals[j] = Interval(
				    min(intI.start, intJ.start), max(intI.end, intJ.end))
				del intervals[i]
				break

	return intervals


# time O(n * log(n)), space O(n)
def merge(intervals: List[Interval]) -> List[Interval]:
	if not intervals or len(intervals) == 0:
		return intervals

	merged = []

	for interval in sorted(intervals):
		if len(merged) == 0 or merged[-1].end < interval.start:
			merged.append(interval)
		elif merged[-1].end < interval.end:
			merged[-1] = merged[-1]._replace(end=interval.end)

	return merged


for i in range(10):
	intervals = [
	    Interval(1, 3),
	    Interval(5, 8),
	    Interval(4, 10),
	    Interval(20, 25),
	    Interval(0, 2),
	    Interval(3, 5),
	    Interval(8, 9),
	    Interval(15, 20),
	    Interval(10, 15),
	    Interval(12, 14),
	    Interval(17, 21)
	]
	shuffle(intervals)
	print(f"   merge({intervals})   = {merge(intervals)}")
	print(f"mergeNCube({intervals}) = {mergeNCube(intervals)}")
