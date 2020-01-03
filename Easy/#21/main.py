"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

from typing import List, NamedTuple


class TimeInterval(NamedTuple):
	start: int
	end: int


# time O(n * log(n) + n * n), space O(n)
def minRoomsV1(timeIntervals: List[TimeInterval]) -> int:
	if len(timeIntervals) == 0:
		return 0

	timeIntervals.sort()

	end = -1
	nonOverlappingIndexes = []
	for i, timeInterval in enumerate(timeIntervals):
		if timeInterval.start >= end:
			end = timeInterval.end
			nonOverlappingIndexes.insert(0, i)

	for i in nonOverlappingIndexes:
		del timeIntervals[i]

	return 1 + minRoomsV1(timeIntervals)


# time O(n * log(n)), space O(n)
def minRoomsV2(timeIntervals: List[TimeInterval]) -> int:
	starts = [t.start for t in timeIntervals]
	ends = [t.end for t in timeIntervals]
	starts.sort()
	ends.sort()

	maxRoom, nowRoom = 0, 0
	startIndex, endIndex = 0, 0
	while startIndex < len(starts) and endIndex < len(ends):
		if starts[startIndex] < ends[endIndex]:
			nowRoom += 1
			startIndex += 1
		else:
			nowRoom -= 1
			endIndex += 1

		if nowRoom > maxRoom:
			maxRoom = nowRoom

	if nowRoom != len(ends) - endIndex:
		print("Schedule seems sketchy...")

	return maxRoom


# time O(n * log(n)), space O(n)
def minRoomsV3(timeIntervals: List[TimeInterval]) -> int:
	starts = [(t.start, 1) for t in timeIntervals]
	ends = [(t.end, -1) for t in timeIntervals]
	roomsAlloc = [t[1] for t in sorted(starts + ends)]

	maxRoom, nowRoom = 0, 0
	for alloc in roomsAlloc:
		nowRoom += alloc
		if nowRoom > maxRoom:
			maxRoom = nowRoom

	if nowRoom != 0:
		print("Schedule seems sketchy...")

	return maxRoom


print(
    f"minRoomsV1([TimeInterval(30, 75), TimeInterval(0, 50), TimeInterval(60, 150)]) = {minRoomsV1([TimeInterval(30, 75), TimeInterval(0, 50), TimeInterval(60, 150)])}"
)
print(
    f"minRoomsV2([TimeInterval(30, 75), TimeInterval(0, 50), TimeInterval(60, 150)]) = {minRoomsV2([TimeInterval(30, 75), TimeInterval(0, 50), TimeInterval(60, 150)])}"
)
print(
    f"minRoomsV3([TimeInterval(30, 75), TimeInterval(0, 50), TimeInterval(60, 150)]) = {minRoomsV3([TimeInterval(30, 75), TimeInterval(0, 50), TimeInterval(60, 150)])}"
)

print(
    f"minRoomsV1([TimeInterval(30, 75), TimeInterval(0, 50), TimeInterval(60, 150), TimeInterval(42, 55), TimeInterval(10, 20), TimeInterval(0, 180), TimeInterval(180, 200), TimeInterval(140, 200)]) = {minRoomsV1([TimeInterval(30, 75), TimeInterval(0, 50), TimeInterval(60, 150), TimeInterval(42, 55), TimeInterval(10, 20), TimeInterval(0, 180), TimeInterval(180, 200), TimeInterval(140, 200)])}"
)
print(
    f"minRoomsV2([TimeInterval(30, 75), TimeInterval(0, 50), TimeInterval(60, 150), TimeInterval(42, 55), TimeInterval(10, 20), TimeInterval(0, 180), TimeInterval(180, 200), TimeInterval(140, 200)]) = {minRoomsV2([TimeInterval(30, 75), TimeInterval(0, 50), TimeInterval(60, 150), TimeInterval(42, 55), TimeInterval(10, 20), TimeInterval(0, 180), TimeInterval(180, 200), TimeInterval(140, 200)])}"
)
print(
    f"minRoomsV3([TimeInterval(30, 75), TimeInterval(0, 50), TimeInterval(60, 150), TimeInterval(42, 55), TimeInterval(10, 20), TimeInterval(0, 180), TimeInterval(180, 200), TimeInterval(140, 200)]) = {minRoomsV3([TimeInterval(30, 75), TimeInterval(0, 50), TimeInterval(60, 150), TimeInterval(42, 55), TimeInterval(10, 20), TimeInterval(0, 180), TimeInterval(180, 200), TimeInterval(140, 200)])}"
)
