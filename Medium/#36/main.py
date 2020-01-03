"""
Given the root to a binary search tree, find the second largest node in the tree.
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
		return f"Node({self.val})"


def nthLargest(root: Node, n: int) -> Node:
	if not root or nthLargest.nbFound >= n:
		return None

	node = nthLargest(root.right, n)
	if node:
		return node

	nthLargest.nbFound += 1
	if nthLargest.nbFound == n:
		return root

	return nthLargest(root.left, n)


def secondLargest(root: Node) -> Node:
	nthLargest.nbFound = 0
	return nthLargest(root, 2)


tree = Node(42, Node(40, Node(35)), Node(50, Node(45), Node(55)))
print(f"secondLargest({tree}) = {secondLargest(tree)}")
