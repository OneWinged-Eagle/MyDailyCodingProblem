"""
Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.
"""

from typing import Any, List


class Stack:
	stack: List[Any]

	def __init__(self):
		self.stack = []

	def push(self, val: Any) -> None:
		if val == None:
			return

		self.stack.append(val)

	def pop(self) -> Any:
		if len(self.stack) == 0:
			return None

		return self.stack.pop()

	def __len__(self):
		return len(self.stack)

	def __repr__(self):
		return f"Stack({self.stack})"


class Queue:
	mainStack: Stack
	reserveStack: Stack

	def __init__(self):
		self.mainStack = Stack()
		self.reserveStack = Stack()

	def enqueue(self, val: Any) -> None:
		if val == None:
			return

		self.mainStack.push(val)

	def dequeue(self) -> Any:
		if len(self.mainStack) == 0:
			return None

		while len(self.mainStack) > 0:
			self.reserveStack.push(self.mainStack.pop())

		val = self.reserveStack.pop()

		while len(self.reserveStack) > 0:
			self.mainStack.push(self.reserveStack.pop())

		return val

	def __len__(self):
		return len(self.mainStack)

	def __repr__(self):
		return f"Queue({self.mainStack})"


myQueue = Queue()
print(f"myQueue = {myQueue}")
print(f"myQueue.dequeue() = {myQueue.dequeue()}")
print(f"myQueue = {myQueue}")
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print(f"myQueue = {myQueue}")
print(f"myQueue.dequeue() = {myQueue.dequeue()}")
print(f"myQueue = {myQueue}")
print(f"myQueue.dequeue() = {myQueue.dequeue()}")
print(f"myQueue = {myQueue}")
myQueue.enqueue(4)
myQueue.enqueue(5)
print(f"myQueue = {myQueue}")
print(f"myQueue.dequeue() = {myQueue.dequeue()}")
print(f"myQueue = {myQueue}")
print(f"myQueue.dequeue() = {myQueue.dequeue()}")
print(f"myQueue = {myQueue}")
print(f"myQueue.dequeue() = {myQueue.dequeue()}")
print(f"myQueue = {myQueue}")
