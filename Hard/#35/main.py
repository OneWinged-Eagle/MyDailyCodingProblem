"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

from typing import List
from sys import stderr


# with n = len(strings), Time O(n), Space O(1)
def rearrange(strings: List[str], s: str, start: int = 0) -> int:
	end = start
	while start < len(strings):
		if strings[start] == s:
			strings[start], strings[end] = strings[end], strings[start]
			end += 1
		start += 1
	return end


# with n = len(rgbs), Time O(n), Space O(1)
def segregate2n(rgbs: List[str]) -> None:
	if not all((char == "R" or char == "G" or char == "B") for char in rgbs):
		print("Unauthorized character detected, exiting...", file=stderr)
		return

	end = rearrange(rgbs, "R")
	rearrange(rgbs, "G", end)


# with n = len(rgbs), Time O(n), Space O(1)
def segregate(rgbs: List[str]) -> None:
	start, i = 0, 0
	end = len(rgbs) - 1

	while i <= end:
		if rgbs[i] == "R":
			rgbs[start], rgbs[i] = rgbs[i], rgbs[start]
			start += 1
			i += 1
		elif rgbs[i] == "G":
			i += 1
		elif rgbs[i] == "B":
			rgbs[i], rgbs[end] = rgbs[end], rgbs[i]
			end -= 1
		else:
			print(f"Unauthorized character '{rgbs[i]}', exiting...", file=stderr)
			return


arr = ["G", "B", "R", "R", "B", "R", "G"]
print(f"Before segregate, arr = {arr}")
segregate(arr)
print(f"After segregate, arr = {arr}")

segregate(["G", "B", "R", "test", "B", "R", "G"])

arr = ["R", "G", "B", "B", "G", "R", "G", "G", "B", "B", "R", "G"]
print(f"Before segregate, arr = {arr}")
segregate(arr)
print(f"After segregate, arr = {arr}")
segregate(arr)
print(f"After (re)segregate, arr = {arr}")
