"""
Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""

from typing import Dict, List


def decode(mapping: Dict[int, List[str]], digits: str) -> List[str]:
	strings = []

	for digit in map(int, digits):
		if digit in mapping:
			if len(strings) == 0:
				strings = mapping[digit]
			else:
				strings = [s + m for s in strings for m in mapping[digit]]

	return strings


print(
    f"decode({{2: ['a', 'b', 'c'], 3: ['d', 'e', 'f']}}, '23') = {decode({2: ['a', 'b', 'c'], 3: ['d', 'e', 'f']}, '23')}"
)
