"""
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

    is_locked, which returns whether the node is locked
    lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
    unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
"""

from __future__ import annotations
from typing import Any


class Node:
	val: Any
	left: Node
	right: Node
	parent: Node
	isLocked: bool
	nbDescendantsLocked: int

	def __init__(self, val: Any, left: Node = None, right: Node = None):
		self.val = val
		if left is not None:
			left.parent = self
		self.left = left
		if right is not None:
			right.parent = self
		self.right = right
		self.parent = None
		self.isLocked = False
		self.nbDescendantsLocked = 0

	def is_locked(self) -> bool:
		return self.isLocked

	def lock(self) -> bool:
		if self.isLocked or self.nbDescendantsLocked > 0:
			return False

		curr = self.parent
		while curr is not None:
			if curr.isLocked:
				return False
			curr = curr.parent

		curr = self.parent
		while curr is not None:
			curr.nbDescendantsLocked += 1
			curr = curr.parent

		self.isLocked = True
		return True

	def unlock(self) -> bool:
		if not self.isLocked:
			return False

		curr = self.parent
		while curr is not None:
			curr.nbDescendantsLocked -= 1
			curr = curr.parent

		self.isLocked = False
		return True

	def __repr__(self):
		return f"Node({self.val}, {'locked' if self.isLocked else 'unlocked'}, {self.nbDescendantsLocked} descendants locked)"


left = Node("l", Node("ll"), Node("lr"))
right = Node("r", Node("rl"), Node("rr"))
root = Node("root", left, right)
print(root)
print(left)
print(right)

print(f"Trying to lock {left}: {left.lock()}")
print(root)
print(left)
print(right)

print(f"Trying to lock {right}: {right.lock()}")
print(root)
print(left)
print(right)

print(f"Trying to lock {root}: {root.lock()}")
print(root)
print(left)
print(right)

print(f"Trying to unlock {left}: {left.unlock()}")
print(root)
print(left)
print(right)

print(f"Trying to unlock {right}: {right.unlock()}")
print(root)
print(left)
print(right)

print(f"Trying to unlock {root}: {root.unlock()}")
print(root)
print(left)
print(right)
