"""
Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""

from __future__ import annotations
from math import inf
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

		return rpz + ")"


def minSum(curr: Node, m: int = 0) -> int:
	if curr is None:
		return m

	return min(minSum(curr.left, m + curr.val), minSum(curr.right, m + curr.val))


tree = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1, Node(-1))))
print(f"minSum({tree}) = {minSum(tree)}")
print(f"minSum({tree.right}) = {minSum(tree.right)}")
tree.right.right.right = Node(-2)
print(f"minSum({tree}) = {minSum(tree)}")
print(f"minSum({tree.right}) = {minSum(tree.right)}")
