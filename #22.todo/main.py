"""
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""

from typing import List


# with d = len(dictionary) and n the number of words in sentence: time O(d * n), space O(n)
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


def sentenceToList(dictionary: List[str], sentence: str) -> List[str]:
	return bruteForce(dictionary, sentence)


sentence1 = sentenceToList(["quick", "brown", "the", "fox"], "thequickbrownfox")
print(
    f"listOfSentence([\"quick\", \"brown\", \"the\", \"fox\"], \"thequickbrownfox\") = {sentence1}"
)

sentence2 = sentenceToList(["bed", "bath", "bedbath", "and", "beyond"],
                           "bedbathandbeyond")
print(
    f"listOfSentence([\"bed\", \"bath\", \"bedbath\", \"and\", \"beyond\"], \"bedbathandbeyond\") = {sentence2}"
)

sentence3 = sentenceToList(["bed", "bedbath", "and", "beyond"],
                           "bedbathandbeyond")
print(
    f"listOfSentence([\"bed\", \"bedbath\", \"and\", \"beyond\"], \"bedbathandbeyond\") = {sentence3}"
)

sentence4 = sentenceToList(["bed", "and", "beyond"], "bedbathandbeyond")
print(
    f"listOfSentence([\"bed\", \"and\", \"beyond\"], \"bedbathandbeyond\") = {sentence4}"
)
