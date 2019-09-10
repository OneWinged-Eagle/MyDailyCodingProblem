"""
Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
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


def merge(lLists: List[SLinkedList]) -> SLinkedList:
	if not lLists or len(lLists) == 0 or all(not lList.head for lList in lLists):
		return None

	mergedList, curr = SLinkedList(), None

	while any(lList.head for lList in lLists):
		smallest, smalls = None, []

		for i, lList in enumerate(lLists):
			if lList.head:
				if smallest == None or lList.head.val < smallest:
					smallest = lList.head.val
					smalls = [i]
				elif lList.head.val == smallest:
					smalls.append(i)

		for i in smalls:
			if mergedList.head == None:
				mergedList.head = Node(lLists[i].head.val)
				curr = mergedList.head
			else:
				curr.next = Node(lLists[i].head.val)
				curr = curr.next

			lLists[i].head = lLists[i].head.next

	return mergedList


l1 = SLinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8])
l2 = SLinkedList([0, 1, 1, 2, 3, 5, 8, 13, 21])
l3 = SLinkedList([0, 2, 4, 6, 8, 10, 12, 14, 16])
print(f"l1 = {l1}")
print(f"l2 = {l2}")
print(f"l3 = {l3}")
print(f"merge([l1, l2, l3]) = {merge([l1, l2, l3])}")
