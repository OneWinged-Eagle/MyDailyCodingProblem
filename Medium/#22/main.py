"""
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""

from typing import List


# with d = len(dictionary) and n the number of words in the sentence: Time O(d * n), Space O(n)
# doesn't work for some cases (sentence3)
def bruteForce(dictionary: List[str], sentence: str) -> List[str]:
	sentenceList = []

	i = 0
	while i < len(sentence):
		gotWord = False
		for word in dictionary:
			if sentence.startswith(word, i):
				sentenceList.append(word)
				gotWord = True
				i += len(word)
		if not gotWord:
			return None

	return sentenceList


# with d = len(dictionary) and n the number of words in the sentence: Time O(d * n), Space O(n)
def helper(dictionary: List[str], sentence: str, words: List[str]) -> List[str]:
	if len(sentence) == 0:
		return words

	for word in dictionary:
		if sentence.startswith(word):
			tmp = helper(dictionary, sentence[len(word):], words + [word])
			if len(tmp) != 0:
				return tmp

	return []


def sentenceToWords(dictionary: List[str], sentence: str) -> List[str]:
	return helper(dictionary, sentence, [])


sentence1 = sentenceToWords(["quick", "brown", "the", "fox"],
                            "thequickbrownfox")
print(
    f"listOfSentence([\"quick\", \"brown\", \"the\", \"fox\"], \"thequickbrownfox\") = {sentence1}"
)

sentence2 = sentenceToWords(["bed", "bath", "bedbath", "and", "beyond"],
                            "bedbathandbeyond")
print(
    f"listOfSentence([\"bed\", \"bath\", \"bedbath\", \"and\", \"beyond\"], \"bedbathandbeyond\") = {sentence2}"
)

sentence3 = sentenceToWords(["bed", "bedbath", "and", "beyond"],
                            "bedbathandbeyond")
print(
    f"listOfSentence([\"bed\", \"bedbath\", \"and\", \"beyond\"], \"bedbathandbeyond\") = {sentence3}"
)

sentence4 = sentenceToWords(["bed", "and", "beyond"], "bedbathandbeyond")
print(
    f"listOfSentence([\"bed\", \"and\", \"beyond\"], \"bedbathandbeyond\") = {sentence4}"
)
