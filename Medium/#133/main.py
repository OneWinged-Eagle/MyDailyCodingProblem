"""
Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35

You can assume each node has a parent pointer.
"""

from __future__ import annotations
from typing import Any, Iterator, Tuple


class Node:
	val: Any
	left: Node
	right: Node
	parent: Node

	def __init__(self,
	             val: Any,
	             left: Node = None,
	             right: Node = None,
	             parent: Node = None):
		self.val = val
		self.left = left
		self.right = right
		self.parent = parent

	def inorder(self) -> Iterator[Node]:
		if self.left is not None:
			yield from self.left.inorder()

		yield self

		if self.right is not None:
			yield from self.right.inorder()

	def __repr__(self):
		return f"Node({self.val})"


def nextInorder(node: Node) -> Node:
	if node is None:
		return None

	root = node

	while root.parent is not None:
		root = root.parent

	inorderGen = root.inorder()

	for n in inorderGen:
		if n == node:
			return next(inorderGen, None)

	return None


root = Node(10)
root.left = Node(5, parent=root)
root.right = Node(30, parent=root)
root.right.left = Node(22, parent=root.right)
root.right.right = Node(35, parent=root.right)

print(f"nextInorder({root.parent}) = {nextInorder(root.parent)}")
print(f"nextInorder({root}) = {nextInorder(root)}")
print(f"nextInorder({root.left}) = {nextInorder(root.left)}")
print(f"nextInorder({root.right}) = {nextInorder(root.right)}")
print(f"nextInorder({root.right.left}) = {nextInorder(root.right.left)}")
print(f"nextInorder({root.right.right}) = {nextInorder(root.right.right)}")
