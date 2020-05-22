"""
Given a binary search tree and a range [a, b] (inclusive), return the sum of the elements of the binary search tree within the range.

For example, given the following tree:

    5
   / \
  3   8
 / \ / \
2  4 6  10

and the range [4, 9], return 23 (5 + 4 + 6 + 8).
"""

from __future__ import annotations
from typing import Any


class Node:
	val: Any
	left: Node
	right: Node

	def __init__(self, val: Any = None, left: Node = None, right: Node = None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		rpz = f"Node({self.val}"

		if self.left or self.right:
			rpz += f", {self.left}"

		if self.right:
			rpz += f", {self.right}"

		return rpz


def sumRange(root: Node, minimum: int, maximum: int) -> int:
	if root == None:
		return 0

	if root.val > minimum and root.val < maximum:
		return root.val + sumRange(root.left, minimum, maximum) + sumRange(
		    root.right, minimum, maximum)

	if root.val == minimum:
		return root.val + sumRange(root.right, minimum, maximum)

	if root.val < minimum:
		return sumRange(root.right, minimum, maximum)

	if root.val == maximum:
		return root.val + sumRange(root.left, minimum, maximum)

	if root.val > maximum:
		return sumRange(root.left, minimum, maximum)

	return 0


tree = Node(5, Node(3, Node(2), Node(4)), Node(8, Node(6), Node(10)))
assert sumRange(tree, 4, 9) == 23
print('passed')
