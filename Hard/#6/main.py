"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""

from typing import Any, Dict


class Node:
	val: Any
	both: int

	def __init__(self, val: Any, both: int):
		self.val = val
		self.both = both

	def __repr__(self):
		return f"Node({repr(self.val)})"


class Memory:
	memory: Dict[int, Node]

	def __init__(self):
		self.memory = {}

	def dereference_ptr(self, ptr: int) -> Node:
		return self.memory[ptr]

	def get_ptr(self, obj: Node) -> int:
		ptr = id(obj)
		self.memory[ptr] = obj
		return ptr


class XORLinkedList:
	memory: Memory
	firstPtr: int
	lastPtr: int

	def __init__(self):
		self.memory = Memory()
		self.firstPtr = 0
		self.lastPtr = 0

	def add(self, val):
		node = Node(val, 0)
		nodePtr = self.memory.get_ptr(node)

		if self.firstPtr == 0:
			self.firstPtr = nodePtr
			self.lastPtr = nodePtr
		else:
			lastNode = self.memory.dereference_ptr(self.lastPtr)
			node.both = self.lastPtr
			lastNode.both ^= nodePtr
			self.lastPtr = nodePtr

	def get(self, index: int) -> Node:
		node = None
		lastPtr = 0
		ptr = self.firstPtr
		for _ in range(index):
			if ptr == 0:
				return None
			node = self.memory.dereference_ptr(ptr)
			lastPtr, ptr = ptr, lastPtr ^ node.both
		return node

	def __repr__(self):
		rpz = ""
		lastPtr = 0
		ptr = self.firstPtr
		while ptr != 0:
			node = self.memory.dereference_ptr(ptr)
			rpz += f"{node} -> "
			lastPtr, ptr = ptr, lastPtr ^ node.both
		return rpz[:-4]


xorList = XORLinkedList()
xorList.add("Hello")
xorList.add("World")
xorList.add("!!!")
print(xorList)
xorList.add("MOAR")
xorList.add("?")
print(xorList)
print(f"xorList.get(0) = {xorList.get(0)}")
print(f"xorList.get(3) = {xorList.get(3)}")
print(f"xorList.get(6) = {xorList.get(6)}")
