"""
Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.
"""

from __future__ import annotations
from random import randint, random
from typing import Any


class Node:
	val: Any
	_left: Node
	_right: Node
	leftDone: bool
	rightDone: bool

	def __init__(self, val: Any, left: Node = None, right: Node = None):
		self.val = val
		self._left = left
		self._right = right
		self.leftDone = False
		self.rightDone = False

	@property
	def left(self) -> Node:
		if not self.leftDone:
			if random() >= 0.5:
				self._left = Node(randint(-255, 255))

			self.leftDone = True

		return self._left

	@property
	def right(self) -> Node:
		if not self.rightDone:
			if random() <= 0.5:
				self._right = Node(randint(-255, 255))

			self.rightDone = True

		return self._right

	def __repr__(self):
		rpz = f"Node({self.val}"

		if self.left or self.right:
			rpz += f", {self.left}"

		if self.right:
			rpz += f", {self.right}"

		return rpz + ")"


def generate() -> Node:
	return Node(randint(-255, 255))


print(f"\ngenerate() = {generate()}\n")

print(f"generate() = {generate()}\n")

print(f"generate() = {generate()}\n")
