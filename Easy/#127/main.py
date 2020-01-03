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
from math import ceil, log
from typing import Any


class Node:
	val: Any
	next: Node

	def __init__(self, val: Any = None, next: Node = None):
		self.val = val
		self.next = next

	def __repr__(self):
		return f"{self.val} -> {self.next}" if self.next else str(self.val)


class NumberList:
	head: Node

	def __init__(self, nb: int):
		node = None
		for n in (
		    (nb // (10**i)) % 10 for i in range(ceil(log(nb, 10)) - 1, -1, -1)):
			node = Node(n, node)
		self.head = node

	def __iter__(self) -> Any:
		curr = self.head
		while curr is not None:
			yield curr.val
			curr = curr.next

	def __add__(self, other: NumberList) -> NumberList:
		summ = 0

		for i, (nb1, nb2) in enumerate(zip_longest(self, other, fillvalue=0)):
			summ += (nb1 + nb2) * 10**i

		return NumberList(summ)

	def __repr__(self):
		nb = 0
		for (i, n) in enumerate(self):
			nb += n * 10**i

		return f"{nb} ({self.head})"


list99 = NumberList(99)
list25 = NumberList(25)
list124 = list99 + list25
print(f"{list99} + {list25} = {list124}")
print(f"{list124} + {list25} = {list124 + list25}")
print(f"{list124} + {list99} = {list124 + list99}")
