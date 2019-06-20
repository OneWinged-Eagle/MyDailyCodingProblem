"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""


class ptr:

	def __init__(self, obj):
		self.obj = obj

	def get(self):
		return self.obj

	def set(self, obj):
		self.obj = obj

	def __del__(self):
		print("ptr deleted")


def dereference_ptr(ptr):
	return ptr.get()


def get_ptr(obj):
	return ptr(obj)


class Node:

	def __init__(self, val, both):
		self.val = val
		self.both = both

	def __del__(self):
		print("node deleted")


class XORLinkedList:

	def __init__(self):
		self.firstPtr = None
		self.lastPtr = None

	def add(self, val):
		node = Node(val, None)
		nodePtr = get_ptr(node)

		if self.firstPtr == None:
			self.firstPtr = nodePtr
			self.lastPtr = nodePtr
		else:
			lastNode = dereference_ptr(self.lastPtr)
			node.both = lastNode.both
			if lastNode.both == None:
				lastNode.both = nodePtr
			else:
				lastNode.both ^= nodePtr

	def print(self):
		i = 0
		ptr = self.firstPtr
		while ptr != None:
			node = dereference_ptr(ptr)
			print(f"Element #{i} = {node.val}")
			i += 1
			ptr ^= node.both


xorList = XORLinkedList()
xorList.add("Hello")
xorList.add("World")
xorList.add("!!!")
xorList.print()
