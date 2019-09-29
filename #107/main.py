"""
Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
"""

from __future__ import annotations
from collections import deque
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


def printLevel(root: Node) -> None:
	if root == None:
		return

	queue = deque([root])

	while (len(queue) > 0):
		curr = queue.popleft()

		print(curr.val, end=' ')

		if curr.left != None:
			queue.append(curr.left)

		if curr.right != None:
			queue.append(curr.right)


root = Node(1, Node(2, None, Node(4)), Node(3, Node(5), Node(6)))
print(f"root = {root}")
printLevel(root)
