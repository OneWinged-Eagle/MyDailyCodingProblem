"""
Implement a stack API using only a heap. A stack implements the following methods:

    push(item), which adds an element to the stack
    pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)

Recall that a heap has the following operations:

    push(item), which adds a new key to the heap
    pop(), which removes and returns the max value of the heap
"""

from heapq import heappop, heappush
from typing import Any, List


class Heap:
	heap: List[Any]

	def __init__(self):
		self.heap = []

	def push(self, val: Any):
		heappush(self.heap, val)

	def pop(self) -> Any:
		return heappop(self.heap)

	def __len__(self) -> int:
		return len(self.heap)


class Stack:
	heap: Heap

	def __init__(self):
		self.heap = Heap()

	def push(self, val: Any):
		self.heap.push((-len(self), val))

	def pop(self) -> Any:
		return self.heap.pop()[1]

	def __len__(self) -> int:
		return len(self.heap)

s = Stack()
assert len(s) == 0
s.push(5)
assert len(s) == 1
s.push(3)
assert len(s) == 2
s.push(2)
assert len(s) == 3
s.push(1)
assert len(s) == 4
s.push(1)
assert len(s) == 5
s.push(0)
assert len(s) == 6
assert s.pop() == 0
assert len(s) == 5
assert s.pop() == 1
assert len(s) == 4
assert s.pop() == 1
assert len(s) == 3
assert s.pop() == 2
assert len(s) == 2
assert s.pop() == 3
assert len(s) == 1
assert s.pop() == 5
assert len(s) == 0
print("passed")
