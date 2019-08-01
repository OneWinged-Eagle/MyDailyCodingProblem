"""
Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g

"""

from __future__ import annotations
from typing import Any, Dict, List


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


# for n = len(preorder), Time O(n), Space O(n)
def helper(preorder: List[Any], inorder: List[Any],
           inorderDict: Dict[Any, int]) -> Node:
	if not preorder or not inorder:
		return None

	root = Node(preorder.pop(0))
	if root.val in inorderDict:
		i = inorderDict[root.val] - inorderDict[inorder[0]]
		root.left = helper(preorder, inorder[:i], inorderDict)
		root.right = helper(preorder, inorder[i + 1:], inorderDict)

	return root


# won't work with duplicate val
def reconstructTree(preorder: List[Any], inorder: List[Any]) -> Node:
	return helper(preorder, inorder, {val: i for i, val in enumerate(inorder)})


print(
    f"reconstructTree(['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g']) = {reconstructTree(['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g'])}"
)
print(
    f"reconstructTree(['a', 'b', 'd', 'e'], ['d', 'b', 'e', 'a']) = {reconstructTree(['a', 'b', 'd', 'e'], ['d', 'b', 'e', 'a'])}"
)
print(
    f"reconstructTree(['a', 'c', 'f', 'g'], ['a', 'f', 'c', 'g']) = {reconstructTree(['a', 'c', 'f', 'g'], ['a', 'f', 'c', 'g'])}"
)
