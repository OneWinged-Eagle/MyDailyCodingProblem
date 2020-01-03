"""
Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""

from __future__ import annotations
from typing import Any, List


class Node:
	val: Any
	next: Node

	def __init__(self, val: Any = None, next: Node = None):
		self.val = val
		self.next = next

	def __repr__(self):
		return f"Node({self.val})" if self.next is None else f"Node({self.val}, {self.next})"


def swap(head: Node) -> Node:
	curr = head

	while curr is not None and curr.next is not None:
		curr.val, curr.next.val = curr.next.val, curr.val
		curr = curr.next.next

	return head


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(f"swap({head}) = {swap(head)}")
