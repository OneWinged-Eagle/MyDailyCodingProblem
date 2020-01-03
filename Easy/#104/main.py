"""
Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
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

		if vals is not None:
			lastNode = None
			for val in vals[::-1]:
				newNode = Node(val, lastNode)
				lastNode = newNode
			self.head = lastNode

	def toList(self) -> List[Any]:
		l = []
		node = self.head
		while node is not None:
			l.append(node.val)
			node = node.next
		return l

	def __repr__(self):
		rpz = "SLinkedList("
		node = self.head
		while node is not None:
			rpz += f"{node} -> "
			node = node.next
		return rpz[:-4] + ")"


def palindrome(lList: SLinkedList) -> bool:
	rev = SLinkedList(lList.toList()[::-1])

	if repr(rev) == repr(lList):
		return True

	return False


lList = SLinkedList([1, 4, 3, 4, 1])
print(f"palindrome(lList) = {palindrome(lList)}")
