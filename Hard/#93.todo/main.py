"""
Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.
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


def isBinarySearchTree(root: Node, minVal: int = -inf,
                       maxVal: int = inf) -> bool:
	if not root:
		return True

	if root.val < minVal or root.val > maxVal:
		return False

	return isBinarySearchTree(root.left, minVal, root.val) and isBinarySearchTree(
	    root.right, root.val, maxVal)


bst = Node(10, Node(8, Node(7), Node(10)), Node(12, Node(10), Node(13)))
print(f"bst = {bst}")
print(f"isBinarySearchTree(bst) = {isBinarySearchTree(bst)}")

notBST = Node(10, Node(8, Node(7), Node(11)), Node(12, Node(9), Node(13)))
print(f"notBST = {notBST}")
print(f"isBinarySearchTree(notBST) = {isBinarySearchTree(notBST)}")
