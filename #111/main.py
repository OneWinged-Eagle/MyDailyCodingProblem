"""
Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""

from typing import Dict, List


def anagrams(word: str, string: str) -> List[int]:
	indices = []

	wordDict = {}
	for char in word:
		wordDict[char] = wordDict.get(char, 0) + 1

	tmpDict = wordDict.copy()
	for i, char in enumerate(string):
		if char in tmpDict:
			tmpDict[char] -= 1

			if tmpDict[char] == 0:
				del tmpDict[char]

			if len(tmpDict) == 0:
				indices.append(i - len(word) + 1)
				tmpDict[string[i - len(word) + 1]] = 1

		else:
			tmpDict = wordDict.copy()

	return indices


print(f"anagrams('ab', 'abxaba') = {anagrams('ab', 'abxaba')}")
