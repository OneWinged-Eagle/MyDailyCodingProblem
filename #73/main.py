"""
Given the head of a singly linked list, reverse it in-place.
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
		return f"Node({self.val})"


class SLinkedList:
	head: Node

	def __init__(self, vals: List[Any] = None):
		self.head = None

		if vals != None:
			lastNode = None
			for val in vals[::-1]:
				newNode = Node(val, lastNode)
				lastNode = newNode
			self.head = lastNode

	def __repr__(self):
		rpz = "SLinkedList("
		node = self.head
		while node != None:
			rpz += f"{node} -> "
			node = node.next
		return rpz[:-4] + ")"


def reverse(lList: SLinkedList) -> None:
	curr, prev = lList.head, None
	while curr.next != None:
		curr.next, prev, curr = prev, curr, curr.next

	curr.next = prev
	lList.head = curr


lList = SLinkedList([8, 5, 3, 2, 1, 0])
print(f"before reverse, lList = {lList}")
reverse(lList)
print(f"after reverse, lList = {lList}")
