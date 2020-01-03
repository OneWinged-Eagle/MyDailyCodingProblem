"""
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5

You should return 45, as it is (3 + 2) * (4 + 5).
"""

from __future__ import annotations
from enum import Enum
from typing import Any


class Operand(Enum):
	ADD = "+"
	SUB = "-"
	MUL = "*"
	DIV = "/"


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


def calculus(root: Node) -> float:
	if not root:
		return 0

	if not root.left and not root.right:
		return root.val

	operand = Operand(root.val)
	if operand == Operand.ADD:
		return calculus(root.left) + calculus(root.right)
	elif operand == Operand.SUB:
		return calculus(root.left) - calculus(root.right)
	elif operand == Operand.MUL:
		return calculus(root.left) * calculus(root.right)
	elif operand == Operand.DIV:
		return calculus(root.left) / calculus(root.right)

	return 0


tree45 = Node("*", Node("+", Node(3), Node(2)), Node("+", Node(4), Node(5)))
print(f"calculus(tree45) = {calculus(tree45)}")

tree20 = Node("/", Node("-", Node(15), Node(5)), Node("/", Node(1), Node(2)))
print(f"calculus(tree20) = {calculus(tree20)}")

tree90 = Node("-", Node("*", Node(10), Node(10)), Node("/", Node(50), Node(5)))
print(f"calculus(tree90) = {calculus(tree90)}")

tree69 = Node("+", Node("*", Node(6), Node(9)), Node("+", Node(6), Node(9)))
print(f"calculus(tree69) = {calculus(tree69)}")
