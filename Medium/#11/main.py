"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries
"""

from typing import List


# With q = len(query) and n = len(strings): time O(q * n), space(n)
def bruteForce(query: str, dictionary: List[str]) -> List[str]:
	autocomplete = list(filter((lambda x: x.startswith(query)), dictionary))

	return autocomplete


class Node:

	def __init__(self, prefix: str):
		self.prefix = prefix
		self.children = {}
		self.isWord = False


def findWords(node: Node) -> List[str]:
	if node.isWord:
		return [node.prefix]
	words = []
	for c in node.children.keys():
		words += findWords(node.children[c])
	return words


def createTrie(dictionary: List[str]) -> Node:
	trie = Node("")
	for s in dictionary:
		curr = trie
		for i, c in enumerate(s):
			if c not in curr.children:
				curr.children[c] = Node(s[:i + 1])
			curr = curr.children[c]
			if i == len(s) - 1:
				curr.isWord = True

	return trie


# Didn't know about "trie", let's try that!
def autocomplete(query: str, dictionary: List[str]) -> List[str]:
	trie = createTrie(dictionary)

	curr = trie
	for c in query:
		if c in curr.children:
			curr = curr.children[c]
		else:
			return []

	return findWords(curr)


a1 = autocomplete("de", ["dog", "deer", "deal"])
print(f"autocomplete(\"de\", [\"dog\", \"deer\", \"deal\"]) = {a1}")
