"""
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
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
		return f"Node({repr(self.val)})"


# Could have added a length member, like in exercice #20, but was maybe a bit too easy that way?
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

	def __repr__(self):
		rpz = ""
		node = self.head
		while node is not None:
			rpz += f"{node} -> "
			node = node.next
		return rpz[:-4]

	def removeFromEnd(self, k: int):
		if k <= 0:
			print(f"k must be strictly positive (k = {k})")
			return

		fastIndex = 0
		fastNode = self.head
		while fastIndex < k and fastNode is not None:
			fastIndex += 1
			fastNode = fastNode.next

		if fastIndex < k:
			print(f"k = {k} isn't valid (length of list = {fastIndex})")
			return

		slowNode = None
		while fastNode is not None:
			fastNode = fastNode.next
			slowNode = slowNode.next if slowNode is not None else self.head

		if slowNode is None:
			self.head = self.head.next
		else:
			slowNode.next = slowNode.next.next


linkedList = SLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(linkedList)
linkedList.removeFromEnd(9)
print(linkedList)
linkedList.removeFromEnd(1)
print(linkedList)
linkedList.removeFromEnd(-1)
print(linkedList)
linkedList.removeFromEnd(0)
print(linkedList)
linkedList.removeFromEnd(8)
print(linkedList)
linkedList.removeFromEnd(4)
print(linkedList)
