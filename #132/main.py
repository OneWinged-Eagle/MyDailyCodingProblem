"""
Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

    record(timestamp): records a hit that happened at timestamp
    total(): returns the total number of hits recorded
    range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?
"""

from __future__ import annotations
from typing import Any, List


class Node:
	val: Any
	left: Node
	right: Node

	def __init__(self, val: Any = None, left: Node = None, right: Node = None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		rpz = f"Node({self.val}"

		if self.left or self.right:
			rpz += f", {self.left}"

		if self.right:
			rpz += f", {self.right}"

		return rpz + ")"


class BST:
	root: Node
	length: int

	def __init__(self):
		self.root = None
		self.length = 0

	def __len__(self):
		return self.length

	def insert(self, data: Any) -> bool:
		if self.root is None:
			self.root = Node(data)
			self.length = 1
			return True

		curr = self.root

		while (42):
			if curr.val == data:
				return False

			if data < curr.val:
				if curr.left is None:
					curr.left = Node(data)
					self.length += 1
					return True

				else:
					curr = curr.left

			else:
				if curr.right is None:
					curr.right = Node(data)
					self.length += 1
					return True

				else:
					curr = curr.right

	def __range__(self, curr: Node, start: Any, end: Any,
	              r: List[Any]) -> List[Any]:
		if curr is None:
			return r

		if start <= curr.val:
			r = self.__range__(curr.left, start, end, r)

		if start <= curr.val <= end:
			r.append(curr.val)

		if curr.val <= end:
			r = self.__range__(curr.right, start, end, r)

		return r

	def range(self, start: Any, end: Any) -> List[Any]:
		if self.root is None:
			return []

		return self.__range__(self.root, start, end, [])

	def __repr__(self):
		return repr(self.root)


class HitCounterBST(BST):

	def __init__(self):
		super().__init__()

	def record(self, timestamp: int):
		self.insert(timestamp)

	def total(self) -> int:
		return len(self)

	def range(self, lower, upper) -> int:
		return len(super().range(lower, upper))


from sortedcontainers import SortedList


class HitCounter:
	records: SortedList

	def __init__(self):
		self.records = SortedList()

	def record(self, timestamp: int):
		self.records.add(timestamp)

	def total(self) -> int:
		return len(self.records)

	def range(self, lower, upper) -> int:
		return sum(1 for _ in self.records.irange(lower, upper))


hc = HitCounter()
hc.record(5)
hc.record(17)
hc.record(1)
hc.record(10)
hc.record(20)
hc.record(2)
hc.record(15)
assert hc.total() == 7
assert hc.range(2, 9) == 2
assert hc.range(0, 42) == 7
assert hc.range(4, 17) == 4
print("passed")
