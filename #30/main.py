"""
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
"""

from typing import List


# time O(n), space O(1)
def trappedWaterUnits(elevation: List[int]) -> int:
	unit = 0

	end = 1
	while end < len(elevation):
		start = end - 1
		indexMaxEnd = end

		while end + 1 < len(elevation) and elevation[end] < elevation[start]:
			end += 1
			if elevation[end] > elevation[indexMaxEnd]:
				indexMaxEnd = end

		for i in range(start + 1, indexMaxEnd):
			unit += min(elevation[start], elevation[indexMaxEnd]) - elevation[i]

		end += 1

	return unit


print(f"trappedWaterUnits([42] = {trappedWaterUnits([42])}")
print(f"trappedWaterUnits([2, 1, 2] = {trappedWaterUnits([2, 1, 2])}")
print(
    f"trappedWaterUnits([3, 0, 1, 3, 0, 5] = {trappedWaterUnits([3, 0, 1, 3, 0, 5])}"
)
print(
    f"trappedWaterUnits([-2, -1, 0, -2, 2, 0, 1, -4, 5, 6, 2, 4, 0, -1] = {trappedWaterUnits([-2, -1, 0, -2, 2, 0, 1, -4, 5, 6, 2, 4, 0, -1])}"
)
