"""
Given a binary tree, return the level of the tree with minimum sum.
"""

from __future__ import annotations
from math import inf
from typing import Any, List, Tuple


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


def helper(nodes: List[Node], lvl: int = 0) -> Tuple[int, int]:
	currSum, children = 0, []

	for node in nodes:
		currSum += node.val

		if node.left is not None:
			children.append(node.left)

		if node.right is not None:
			children.append(node.right)

	if len(children) != 0:
		return min((currSum, lvl), helper(children, lvl + 1))

	return (currSum, lvl)


def minSumLvl(root: Node) -> int:
	if root is None:
		return 0

	return helper([root])[1]


root = Node(100, Node(10, Node(40)), Node(10))
print(f"minSumLvl({root}) = {minSumLvl(root)}")
root.left.left.val = 10
print(f"minSumLvl({root}) = {minSumLvl(root)}")
root.left.left.right = Node(-10)
print(f"minSumLvl({root}) = {minSumLvl(root)}")
