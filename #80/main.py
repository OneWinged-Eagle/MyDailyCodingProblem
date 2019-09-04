"""
Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
"""

from __future__ import annotations
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
		return f"Node({self.val}, {self.left}, {self.right})"


def helper(root: Node, level: int = 0) -> Tuple[Node, int]:
	if not root.left and not root.right:
		return root, level

	left, right = (None, 0), (None, 0)

	if root.left:
		left = helper(root.left, level + 1)

	if root.right:
		right = helper(root.right, level + 1)

	return left if left[1] >= right[1] else right


def deepest(root: Node) -> Node:
	if not root:
		return None

	return helper(root)[0]


root = Node("root", Node("l", Node("ll"), Node("lr")),
            Node("r", Node("rl"), Node("rr")))
print(f"deepest(root) = {deepest(root)}")
root = Node("root", Node("l", Node("ll", None, Node("llr")), Node("lr")),
            Node("r", Node("rl"), Node("rr")))
print(f"deepest(root) = {deepest(root)}")
root = Node("root", Node("l", Node("ll"), Node("lr")),
            Node("r", Node("rl"), Node("rr", Node("rrl"))))
print(f"deepest(root) = {deepest(root)}")
