"""
Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15

Return the nodes 5 and 15.
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
		rpz = f"Node({self.val}"

		if self.left or self.right:
			rpz += f", {self.left}"

		if self.right:
			rpz += f", {self.right}"

		return rpz + ")"


def twoNodesSumTo(root: Node, K: int) -> Tuple[Node, Node]:
	if root == None or root.left == None and root.right == None:
		return None

	return (root.left, root.right)


root = Node(10, Node(5), Node(15, Node(11), Node(15)))
print(f"twoNodesSumTo({root}) = {twoNodesSumTo(root, 20)}")
