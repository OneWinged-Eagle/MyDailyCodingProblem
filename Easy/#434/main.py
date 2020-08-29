"""
Given a binary search tree, find the floor and ceiling of a given integer. The floor is the highest element in the tree less than or equal to an integer, while the ceiling is the lowest element in the tree greater than or equal to an integer.

If either value does not exist, return None.
"""

from math import inf
from typing import Any, Tuple


class Node:
	val: Any
	left: Node
	right: Node

	def __init__(self, val: Any, left: Node = None, right: Node = None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		rpz = f"Node({self.val}"

		if self.left or self.right:
			rpz += f", {self.left}"

		if self.right:
			rpz += f", {self.right}"

		return rpz + ")"


def getFloorAndCeiling(root: Node, nb: int) -> Tuple[int, int]:
	floor, ceiling = -inf, inf

	if root.val <= nb:
		floor = root.val

	if root.val >= nb:
		ceiling = root.val

	leftFloor, leftCeiling = getFloorAndCeiling(root.left, nb)

	rightFloor, rightCeiling = getFloorAndCeiling(root.right, nb)

	floor, ceiling = max(floor, leftFloor,
	                     rightFloor), min(ceiling, leftCeiling, rightCeiling)

	if floor == -inf or ceiling == inf:
		return None

	return floor, ceiling
