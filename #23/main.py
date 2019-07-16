"""
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""

from math import inf
import numpy as np
from typing import List, NamedTuple


class Coordinate(NamedTuple):
	y: int
	x: int


# with y = maze.shape[0] and x = maze.shape[1], Time O(y * x), space O(1)
def minSteps(maze: List[List[bool]], start: Coordinate, end: Coordinate) -> int:
	if start.y < 0 or start.y >= maze.shape[0] or \
                            start.x < 0 or start.x >= maze.shape[1] or \
                      maze[start.y][start.x]:
		return inf

	if start == end:
		return 0

	maze[start.y][start.x] = True

	return 1 + min(
	    minSteps(maze, Coordinate(start.y - 1, start.x), end),
	    minSteps(maze, Coordinate(start.y, start.x + 1), end),
	    minSteps(maze, Coordinate(start.y + 1, start.x), end),
	    minSteps(maze, Coordinate(start.y, start.x - 1), end))


maze = [[False, False, False, False], \
    [True, True, False, True], \
    [False, False, False, False], \
    [False, False, False, False]]
print(
    f"minSteps({maze}, (3, 0), (0, 0)) = {minSteps(np.array(maze), Coordinate(3, 0), Coordinate(0, 0))}"
)

maze = [[False, False, False, False], \
    [True, True, True, False], \
    [True, False, False, False], \
    [False, False, False, True]]
print(
    f"minSteps({maze}, (3, 0), (0, 0)) = {minSteps(np.array(maze), Coordinate(3, 0), Coordinate(0, 0))}"
)

maze = [[False, False, False, False], \
    [True, True, True, True], \
    [True, False, False, False], \
    [False, False, False, True]]
print(
    f"minSteps({maze}, (3, 0), (0, 0)) = {minSteps(np.array(maze), Coordinate(3, 0), Coordinate(0, 0))}"
)
