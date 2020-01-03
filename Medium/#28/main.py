"""
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

from math import ceil
from typing import List


# with w = len(words), time O(w), space O(1)
def balanceSpaces(words: List[str], k: int) -> str:
	nbSpaces = k - sum(len(w) for w in words)
	nbBlank = len(words) - 1

	for i in range(len(words)):
		spaces = ceil(nbSpaces / nbBlank) if nbBlank > 0 else nbSpaces
		words[i] += " " * spaces
		nbSpaces -= spaces
		nbBlank -= 1

	return "".join(words)

# with w = len(words), time O(w), space O(w)
def justify(words: List[str], k: int) -> List[str]:
	lines = []

	length = 0
	prevIndex = 0
	for i, word in enumerate(words):
		if length != 0:
			length += 1
		if length + len(word) > k:
			lines.append(balanceSpaces(words[prevIndex:i], k))
			length = 0
			prevIndex = i
		length += len(word)

	if length > 0:
		lines.append(balanceSpaces(words[prevIndex:], k))

	return lines


for i in range(32):
	print(
	    f"justify(['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.'], {i}) = {justify(['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.'], i)}"
	)
