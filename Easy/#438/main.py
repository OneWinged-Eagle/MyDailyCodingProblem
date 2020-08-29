"""
Implement a stack API using only a heap. A stack implements the following methods:

    push(item), which adds an element to the stack
    pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)

Recall that a heap has the following operations:

    push(item), which adds a new key to the heap
    pop(), which removes and returns the max value of the heap
"""

from typing import Any, List
from heapq import heappop, heappush


class Stack:
	heap: List[Any]

	def __init__(self):
		self.heap = list()

	def push(self, item: Any):
		heappush(self.heap, (-len(self.heap), item))

	def pop(self) -> Any:
		if (len(self.heap) == 0):
			return None

		return heappop(self.heap)[1]


stack = Stack()

stack.push(3)
stack.push(2)
stack.push(1)

assert stack.pop() == 1
assert stack.pop() == 2

stack.push(2.5)

assert stack.pop() == 2.5
assert stack.pop() == 3
assert stack.pop() == None

print("Passed!")
