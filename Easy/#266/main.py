"""
A step word is formed by taking a given word, adding a letter, and anagramming the result. For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".

Given a dictionary of words and an input word, create a function that returns all valid step words.
"""

from collections import Counter
from typing import List, Set


def getStepWords(word: str, dictionary: Set[str]) -> List[str]:
	stepWords = list()

	wordCounter = Counter(word)
	for w in dictionary:
		tmpCounter = wordCounter.copy()

		tmpCounter.subtract(Counter(w))
		if sum(map(abs, tmpCounter.values())) == 1:
			stepWords.append(w)

	return stepWords


dictionary = set(["appeal", "paella", "apple", "apilea", "aapple"])
print(
    f"getStepWords(apple, {dictionary}) = {getStepWords('apple', dictionary)}")
