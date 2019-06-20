"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""


class Node:

	def __init__(self, element, both):
		self.element = element
		self.both = both


class XORLinkedList:

	def __init__(self):
		self.firstNodeId = 0

	def add(self, element):
		if self.firstNodeId == 0:
			self.firstNodeId = id(Node(element, 0))
		else:
			pass


import ctypes
a = "hello world"
print(ctypes.cast(id(a), ctypes.py_object).value)
