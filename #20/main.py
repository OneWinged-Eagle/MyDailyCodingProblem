"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
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


class SLinkedList:
	head: Node
	length: int

	def __init__(self, vals: List[Any] = None):
		self.head = None
		self.length = 0
		if vals != None:
			lastNode = None
			for val in vals[::-1]:
				newNode = Node(val, lastNode)
				lastNode = newNode
				self.length += 1
			self.head = lastNode

	def __repr__(self):
		rpz = ""
		node = self.head
		while node != None:
			rpz += f"{node} -> "
			node = node.next
		return rpz[:-4]


def intersectingNode(list1: SLinkedList, list2: SLinkedList) -> Node:
	node1 = list1.head
	node2 = list2.head
	if list1.length > list2.length:
		for _ in range(list2.length, list1.length):
			node1 = node1.next
	elif list2.length > list1.length:
		for _ in range(list1.length, list2.length):
			node2 = node2.next

	intersect = None
	while node1 != None and node2 != None:
		if node1.val == node2.val and intersect == None:
			intersect = node1
		elif node1.val != node2.val and intersect != None:
			intersect = None
		node1 = node1.next
		node2 = node2.next

	return intersect


l1 = SLinkedList([3, 7, 0, 10])
print(f"l1 = {l1}")
l2 = SLinkedList([99, 1, 0, 10])
print(f"l2 = {l2}")

intersect = intersectingNode(l1, l2)
print(f"intersectingNode(l1, l2) = {intersect}")

l1 = SLinkedList([4, 3, 7, -666, 10])
print(f"l1 = {l1}")
l2 = SLinkedList([99, 1, -666, 10])
print(f"l2 = {l2}")

intersect = intersectingNode(l1, l2)
print(f"intersectingNode(l1, l2) = {intersect}")

l1 = SLinkedList([4, 3, 7, "test", 10])
print(f"l1 = {l1}")
l2 = SLinkedList([42, 1337, 99, 1, "test", 10])
print(f"l2 = {l2}")

intersect = intersectingNode(l1, l2)
print(f"intersectingNode(l1, l2) = {intersect}")

l1 = SLinkedList([4, 3, 7, "nope", 10, 1, "yep", 24])
print(f"l1 = {l1}")
l2 = SLinkedList([0, 42, 1337, 99, 1, "nope", 10, -1, "yep", 24])
print(f"l2 = {l2}")

intersect = intersectingNode(l1, l2)
print(f"intersectingNode(l1, l2) = {intersect}")
