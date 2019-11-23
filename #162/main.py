"""
Given a list of words, return the shortest unique prefix of each word. For example, given the list:

    dog
    cat
    apple
    apricot
    fish

Return the list:

    d
    c
    app
    apr
    f
"""

from __future__ import annotations
from typing import Dict, List


class Node:
	char: str
	count: int
	children: Dict[str, Node]

	def __init__(self, char: str):
		self.char = char
		self.count = 1
		self.children = dict()

	def __repr__(self):
		return f"Node({self.char}, {self.count})"


class Trie:
	head: Node

	def __init__(self, words: List[str]):
		self.head = Node("")

		for word in words:
			curr = self.head
			for char in word:
				if char in curr.children:
					curr.children[char].count += 1
				else:
					curr.children[char] = Node(char)
				curr = curr.children[char]

	def __repr__(self):
		rpz = ""

		stack = [self.head]
		while (len(stack)):
			node = stack.pop()

			rpz += f"{node} -> "

			if len(node.children) == 0:
				rpz += "END\n"

			for n in node.children.values():
				stack.append(n)

		return rpz


def prefixes(words: List[str]) -> List[str]:
	trie = Trie(words)
	p = []

	for word in words:
		curr = trie.head

		for i, char in enumerate(word):
			if curr.children[char].count == 1:
				p.append(word[:i + 1])
				break

			curr = curr.children[char]

		if len(curr.children) == 0:
			p.append(None)

	return p


print(
    f"prefixes(['dog', 'cat', 'apple', 'apricot', 'fish']) = {prefixes(['dog', 'cat', 'apple', 'apricot', 'fish'])}"
)
