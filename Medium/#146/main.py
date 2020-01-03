"""
Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0

should be pruned to:

   0
  / \
 1   0
    /
   1

We do not remove the tree at the root or its left child because it still has a 1 as a descendant.
"""

from __future__ import annotations


class Node:
	val: bool
	left: Node
	right: Node

	def __init__(self, val: bool = False, left: Node = None, right: Node = None):
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


def prune(root: Node) -> Node:
	if not root:
		return None

	root.left = prune(root.left)
	root.right = prune(root.right)

	if not root.val and not root.left and not root.right:
		return None

	return root


root = Node(
    False, Node(True),
    Node(False, Node(True, Node(False), Node(False)),
         Node(False, Node(False), Node(False))))
print(f"prune({root}) = {prune(root)}")
