"""
Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere in the linked list, deep clone the list.
"""

from __future__ import annotations
from typing import Any


class Node:
	val: Any
	next: Node
	random: Node

	def __init__(self, val: Any = None, next: Node = None, random: Node = None):
		self.val = val
		self.next = next
		self.random = random

	def __repr__(self):
		rpz = f"Node({self.val})"

		if self.next is not None:
			rpz += f" with next = Node({self.next.val})"

		if self.random is not None:
			rpz += f" with random = Node({self.random.val})"

		return rpz + "\n" + repr(self.next)


def deepCopy(head: Node) -> Node:
	curr = head

	while curr != None:
		curr.next = Node(curr.val, curr.next)
		curr = curr.next.next

	copy = head.next

	curr = head
	cp = copy

	while cp != None:
		cp.random = curr.random.next
		curr = curr.next.next if curr.next is not None else None
		cp = cp.next.next if cp.next is not None else None

	curr = head
	cp = copy

	while curr != None:
		curr.next = curr.next.next if curr.next is not None else None
		curr = curr.next
		cp.next = curr.next if curr is not None else None
		cp = cp.next

	return copy


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
head.random = head.next.next
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next
head.next.next.next.next.random = head.next.next.next

copy = deepCopy(head)

copy.next.next.val = 42
copy.next.next.random.val = 69

assert copy.val == 1
assert head.random.val == 3
assert copy.random.val == 42

assert copy.next.val == 2
assert copy.next.random.val == 1

assert head.next.next.val == 3
assert copy.next.next.val == 42
assert head.next.next.random.val == 5
assert copy.next.next.random.val == 69

assert copy.next.next.next.val == 4
assert copy.next.next.next.random.val == 2

assert head.next.next.next.next.val == 5
assert copy.next.next.next.next.val == 69
assert copy.next.next.next.next.random.val == 4

print("passed")
