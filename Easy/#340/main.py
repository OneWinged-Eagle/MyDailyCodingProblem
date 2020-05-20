"""
Given a set of points (x, y) on a 2D cartesian plane, find the two closest points. For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)].
"""

from math import sqrt
from typing import List, Tuple


def dist(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
	return sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) *
	            (p1[1] - p2[1]))


def mid(points: List[Tuple[int, int]],
        d: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
	segment = [
	    point for point in points
	    if abs(point[0] - points[len(points) // 2][0]) <= d
	]

	middle = (segment[0], segment[1])
	distMiddle = dist(segment[0], segment[1])
	for i, point in enumerate(segment):
		for p in segment[i + 1:]:
			d = dist(point, p)
			if d < distMiddle:
				middle = (point, p)
				distMiddle = d

	return middle


def helper(points: List[Tuple[int, int]]
          ) -> Tuple[Tuple[int, int], Tuple[int, int]]:
	if len(points) == 2:
		return points

	if len(points) == 3:
		d01, d02, d12 = dist(points[0], points[1]), dist(points[0],
		                                                 points[2]), dist(
		                                                     points[1], points[2])

		if d01 < d02 and d01 < d12:
			return (points[0], points[1])

		if d02 < d01 and d02 < d12:
			return (points[0], points[2])

		return (points[1], points[2])

	left, right = helper(points[:len(points) // 2]), helper(points[len(points) //
	                                                               2:])

	distLeft, distRight = dist(left[0], left[1]), dist(right[0], right[1])

	middle = mid(points, min(distLeft, distRight))
	distMiddle = dist(middle[0], middle[1])

	if distLeft < distRight and distLeft < distMiddle:
		return left

	if distRight < distLeft and distRight < distMiddle:
		return right

	return middle


def closest(points: List[Tuple[int, int]]
           ) -> Tuple[Tuple[int, int], Tuple[int, int]]:
	if len(points) <= 2:
		return points

	points.sort()

	return helper(points)


c = closest([(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)])
assert c == ((1, 1), (-1, -1)) or c == ((-1, -1), (1, 1))
print('passed')
