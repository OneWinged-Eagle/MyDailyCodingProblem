"""
Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

    set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
    get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
"""

from __future__ import annotations
from typing import Any, Dict


class Node:
	key: Any
	val: Any
	next: Node
	prev: Node

	def __init__(self, key: Any, val: Any, next: Node = None, prev: Node = None):
		self.key = key
		self.val = val
		self.next = next
		self.prev = prev

	def __repr__(self):
		return f"Node({self.key}: {self.val})"


class DoublyLinkedList:
	first: Node
	last: Node

	def __init__(self):
		self.first = None
		self.last = None

	def pushFront(self, key: Any, val: Any) -> Node:
		if self.first is None:
			self.first = self.last = Node(key, val)
		else:
			self.first = Node(key, val, self.first)
			self.first.next.prev = self.first

		return self.first

	def pop(self) -> Any:
		if not self.last:
			return None

		key = self.last.key
		self.last = self.last.prev

		if self.last:
			self.last.next = None
		else:
			self.first = None

		return key

	def moveFront(self, node: Node) -> None:
		if not node.prev:
			return

		if node == self.last:
			self.last = self.last.prev

		node.prev.next = node.next
		if node.next:
			node.next.prev = node.prev

		node.next = self.first
		node.prev = None
		self.first = node
		self.first.next.prev = self.first

	def __repr__(self):
		rpz = ""
		curr = self.first
		while curr:
			rpz += f"{curr} -> "
			curr = curr.next
		return rpz[:-4]


class Cache:
	cache: Dict[Any, Node]
	recent: DoublyLinkedList
	length: int
	size: int

	def __init__(self, n: int):
		self.cache = dict()
		self.recent = DoublyLinkedList()
		self.length = 0
		self.size = n

	def set(self, key: Any, value: Any) -> None:
		self.cache[key] = self.recent.pushFront(key, value)

		if self.length == self.size:
			self.cache.pop(self.recent.pop())
		else:
			self.length += 1

	def get(self, key: Any) -> Any:
		if key in self.cache:
			node = self.cache[key]
			self.recent.moveFront(node)
			return node.val
		return None

	def __repr__(self):
		return f"Cache({self.cache}, {self.recent})"


cache = Cache(4)

print(f"cache.get(1) = {cache.get(1)}")

cache.set(1, "one")
print(f"after cache.set(1, 'one'), cache = {cache}")

print(f"cache.get(1) = {cache.get(1)}")

cache.set(2, "two")
print(f"after cache.set(2, 'two'), cache = {cache}")

print(f"cache.get(1) = {cache.get(1)}")

cache.set(3, "three")
print(f"after cache.set(3, 'three'), cache = {cache}")

cache.set(4, "four")
print(f"after cache.set(4, 'four'), cache = {cache}")

cache.set(5, "five")
print(f"after cache.set(5, 'five'), cache = {cache}")
