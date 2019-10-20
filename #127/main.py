"""
Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5

is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9

5 -> 2

return 124 (99 + 25) as:

4 -> 2 -> 1

"""

from __future__ import annotations
from itertools import zip_longest
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

		if vals is not None and len(vals) > 0:
			lastNode = None
			for val in vals[::-1]:
				newNode = Node(val, lastNode)
				lastNode = newNode
			self.head = lastNode
		else:
			self.head = Node()

	def __iter__(self) -> Any:
		curr = self.head
		while curr is not None:
			yield curr.val
			curr = curr.next

	def __add__(self, other: SLinkedList) -> SLinkedList:
		summ = []

		ret = 0
		for (nb1, nb2) in zip_longest(self, other, fillvalue=0):
			n = nb1 + nb2 + ret
			summ.append(n % 10)
			ret = n // 10

		if ret != 0:
			summ.append(ret)

		return SLinkedList(summ)

	def __repr__(self):
		rpz = "SLinkedList("
		node = self.head
		while node is not None:
			rpz += f"{node} -> "
			node = node.next
		return rpz[:-4] + ")"


list99 = SLinkedList([9, 9])
list25 = SLinkedList([5, 2])
list124 = list99 + list25
print(f"{list99} + {list25} = {list124}")
print(f"{list124} + {list25} = {list124 + list25}")
