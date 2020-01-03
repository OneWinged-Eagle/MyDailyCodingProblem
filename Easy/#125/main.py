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
from typing import Any, Iterator, Tuple


class Node:
	val: Any
	left: Node
	right: Node

	def __init__(self, val: Any, left: Node = None, right: Node = None):
		self.val = val
		self.left = left
		self.right = right

	def inorder(self) -> Iterator[Node]:
		if self.left is not None:
			yield from self.left.inorder()

		yield self

		if self.right is not None:
			yield from self.right.inorder()

	def reverseInorder(self) -> Iterator[Node]:
		if self.right is not None:
			yield from self.right.reverseInorder()

		yield self

		if self.left is not None:
			yield from self.left.reverseInorder()

	def __repr__(self):
		rpz = f"Node({self.val}"

		if self.left or self.right:
			rpz += f", {self.left}"

		if self.right:
			rpz += f", {self.right}"

		return rpz + ")"


def twoNodesSumTo(root: Node, K: int) -> Tuple[Node, Node]:
	if root is None:
		return None

	inorderGen, revInorderGen = root.inorder(), root.reverseInorder()
	inorderNode, revInorderNode = next(inorderGen), next(revInorderGen)

	while inorderNode is not None and revInorderNode is not None and inorderNode.val <= revInorderNode.val:
		summ = inorderNode.val + revInorderNode.val

		if summ < K:
			inorderNode = next(inorderGen, None)

		elif summ > K:
			revInorderNode = next(revInorderGen, None)

		else:
			return (inorderNode, revInorderNode)

	return None


root = Node(10, Node(5), Node(15, Node(11), Node(15)))
print(f"twoNodesSumTo({root}, 0) = {twoNodesSumTo(root, 0)}")
print(f"twoNodesSumTo({root}, 15) = {twoNodesSumTo(root, 15)}")
print(f"twoNodesSumTo({root}, 16) = {twoNodesSumTo(root, 16)}")
print(f"twoNodesSumTo({root}, 20) = {twoNodesSumTo(root, 20)}")
print(f"twoNodesSumTo({root}, 21) = {twoNodesSumTo(root, 21)}")
print(f"twoNodesSumTo({root}, 25) = {twoNodesSumTo(root, 25)}")
print(f"twoNodesSumTo({root}, 26) = {twoNodesSumTo(root, 26)}")
print(f"twoNodesSumTo({root}, 42) = {twoNodesSumTo(root, 42)}")

print(f"twoNodesSumTo(None, 42) = {twoNodesSumTo(None, 42)}")

root = Node(10, Node(5))
print(f"twoNodesSumTo({root}, 0) = {twoNodesSumTo(root, 0)}")
print(f"twoNodesSumTo({root}, 15) = {twoNodesSumTo(root, 15)}")
print(f"twoNodesSumTo({root}, 16) = {twoNodesSumTo(root, 16)}")
