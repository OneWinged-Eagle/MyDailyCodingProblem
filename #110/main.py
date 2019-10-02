"""
Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5

Return [[1, 2], [1, 3, 4], [1, 3, 5]].
"""

from __future__ import annotations
from collections import deque
from typing import Any, List


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


def paths(root: Node, base: List[Any] = []) -> List[List[Any]]:
	if root == None:
		return None

	b = base + [root.val]

	left, right = paths(root.left, b), paths(root.right, b)

	if left != None and right != None:
		return left + right
	elif left != None:
		return left
	elif right != None:
		return right

	return [b]


root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print(f"paths({root}) = {paths(root)}")

root = Node(1, Node(2, None, Node(4)),
            Node(3, Node(5), Node(6, Node(7, Node(9)), Node(8))))
print(f"paths({root}) = {paths(root)}")
