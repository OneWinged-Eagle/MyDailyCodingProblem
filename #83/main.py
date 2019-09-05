"""
Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f

should become:

  a
 / \
 c  b
 \  / \
  f e  d
"""

from __future__ import annotations
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


def reverse(root: Node) -> Node:
	if not root:
		return None

	reverse(root.left)
	reverse(root.right)

	root.left, root.right = root.right, root.left

	return root

root = Node("root", Node("r", Node("rr"), Node("rl")),
            Node("l", Node("lr"), Node("ll", Node("llr"))))
print(f"     root     = {root}")
print(f"reverse(root) = {reverse(root)}")
