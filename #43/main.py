"""
Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
    max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
"""

from collections import deque
from typing import Any


class Stack:
	stack: deque
	maxStack: deque

	def __init__(self):
		self.stack = deque()
		self.maxStack = deque()

	def push(self, val: Any) -> None:
		self.stack.append(val)

		if not self.maxStack or val > self.maxStack[-1]:
			self.maxStack.append(val)
		else:
			self.maxStack.append(self.maxStack[-1])

	def pop(self) -> Any:
		if not self.stack:
			return None

		self.maxStack.pop()
		return self.stack.pop()

	def max(self) -> Any:
		if not self.stack:
			return None

		return self.maxStack[-1]


stack = Stack()
print(f"stack.max() = {stack.max()}")
print(f"stack.pop() = {stack.pop()}")
stack.push(42)
stack.push(323)
stack.push(54)
stack.push(666)
stack.push(42)
stack.push(323)
print(f"stack.max() = {stack.max()}")
print(f"stack.pop() = {stack.pop()}")
print(f"stack.max() = {stack.max()}")
print(f"stack.pop() = {stack.pop()}")
print(f"stack.max() = {stack.max()}")
print(f"stack.pop() = {stack.pop()}")
print(f"stack.max() = {stack.max()}")
print(f"stack.pop() = {stack.pop()}")
print(f"stack.max() = {stack.max()}")
print(f"stack.pop() = {stack.pop()}")
print(f"stack.max() = {stack.max()}")
print(f"stack.pop() = {stack.pop()}")
print(f"stack.max() = {stack.max()}")
print(f"stack.pop() = {stack.pop()}")
