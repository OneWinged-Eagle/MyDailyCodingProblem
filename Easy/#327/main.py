"""
Write a program to merge two binary trees. Each node in the new tree should hold a value equal to the sum of the values of the corresponding nodes of the input trees.

If only one input tree has a node in a given position, the corresponding node in the new tree should match that input node.
"""

from __future__ import annotations
from typing import Any


class Node:
	val: Any
	left: Node
	right: Node

	def __init__(self, val: Any = None, left: Node = None, right: Node = None):
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


def merge(rootA: Node, rootB: Node) -> Node:
	if rootA == None:
		return rootB

	if rootB == None:
		return rootA

	return Node(rootA.val + rootB.val, merge(rootA.left, rootB.left),
	            merge(rootA.right, rootB.right))


rootA = Node(0.5, Node(0, Node(4), Node(5)), Node(3))
rootB = Node(0.5, Node(2), Node(0, Node(6), Node(7)))
print(f"merge({rootA}, {rootB}) = {merge(rootA, rootB)}")
