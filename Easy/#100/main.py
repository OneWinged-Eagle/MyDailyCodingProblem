"""
You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)

You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2

It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""

from typing import List, NamedTuple


class Point(NamedTuple):
	x: int
	y: int


def steps(points: List[Point]) -> int:
	if not points or len(points) <= 1:
		return 0

	steps = 0
	for i, point in enumerate(points[:-1]):
		steps += max(abs(point.x - points[i + 1].x), abs(point.y - points[i + 1].y))

	return steps


points = [Point(0, 0), Point(1, 1), Point(1, 2)]
print(f"steps({points}) = {steps(points)}")

points = [Point(-3, 5), Point(0, 0), Point(43, 1), Point(2, -20)]
print(f"steps({points}) = {steps(points)}")
