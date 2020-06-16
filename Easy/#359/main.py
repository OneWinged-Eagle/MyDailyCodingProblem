"""
You are given a string formed by concatenating several words corresponding to the integers zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'. Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order. In the example above, this would be 357.
"""

from collections import Counter
from typing import List

numbersStr = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine"
]
strCounters = [Counter(str) for str in numbersStr]


def helper(count: Counter) -> List[int]:
	for i, strCounter in enumerate(strCounters):
		newCount = count.copy()
		newCount.subtract(strCounter)

		if all([x >= 0 for x in newCount.values()]):
			if all([x == 0 for x in newCount.values()]):
				return [i]

			n = helper(newCount)
			if len(n) > 0:
				return [i] + n

	return []


def parse(anagram: str) -> List[int]:
	return helper(Counter(anagram))


assert parse("niesevehrtfeev") == [3, 5, 7]
assert parse("znieeseverhrtfeevo") == [0, 3, 5, 7]
print('passed')
