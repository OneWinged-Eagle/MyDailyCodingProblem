"""
Given a binary tree of integers, find the maximum path sum between two nodes. The path must go through at least one node, and does not need to go through the root.
"""

from __future__ import annotations
from math import inf
from typing import Any


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


def helper(root: Node) -> int:
	if not root:
		return 0

	left, right = helper(root.left), helper(root.right)

	maxLR = max(max(left, right) + root.val, root.val)

	helper.max = max(helper.max, max(maxLR, left + right + root.val))

	return maxLR


def maxPathSum(root: Node) -> int:
	helper.max = -inf
	helper(root)
	return helper.max


tree = Node(-1, Node(3, Node(1)), Node(4, Node(2), Node(-2, Node(7))))
print(f"maxPathSum({tree}) = {maxPathSum(tree)}")
tree.left.left.val = 3
print(f"maxPathSum({tree}) = {maxPathSum(tree)}")
tree.val = -10
print(f"maxPathSum({tree}) = {maxPathSum(tree)}")
