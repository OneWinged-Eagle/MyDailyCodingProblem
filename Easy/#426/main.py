"""
Given a binary tree, return the level of the tree with minimum sum.
"""

from __future__ import annotations

from itertools import zip_longest
from math import inf
from typing import List


class Node:
	val: int
	left: Node
	right: Node

	def __init__(self, val: int, left: Node = None, right: Node = None):
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


def getLevels(root: Node) -> List[int]:
	if not root:
		return []

	leftLevels, rightLevels = getLevels(root.left), getLevels(root.right)
	return [root.val] + [
	    x + y for x, y in zip_longest(leftLevels, rightLevels, fillvalue=0)
	]


def minLevel(root: Node) -> int:
	levels = getLevels(root)
	return levels.index(min(levels))


test0 = Node(0, Node(1, Node(1)), Node(1, None, Node(1)))
assert minLevel(test0) == 0

test1 = Node(1, Node(0, Node(1)), Node(0, None, Node(1)))
assert minLevel(test1) == 1

test2 = Node(1, Node(1, Node(0)), Node(1, None, Node(0)))
assert minLevel(test2) == 2

print("passed")
