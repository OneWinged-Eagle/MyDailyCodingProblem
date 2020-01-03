"""
Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
"""

from typing import List


# with n = len(string), time O(n), space O(n)
def wrap(string: str, k: int) -> List[str]:
	lines = []

	i = 0
	prevIndex = 0
	line = ""

	while i <= len(string):
		if i >= len(string) or string[i] == ' ' or string[i] == '\t':
			if i - prevIndex > k:
				return None

			if len(line + string[prevIndex:i]) > k:
				lines.append(line)
				line = ""

			if line:
				line += ' '

			line += string[prevIndex:i]

			while i < len(string) and (string[i] == ' ' or string[i] == '\t'):
				i += 1

			prevIndex = i

		i += 1

	if line:
		lines.append(line)

	return lines


for i in range(50):
	print(
	    f"wrap('Waltz, bad nymph, for quick jigs vex.', {i}) = {wrap('Waltz, bad nymph, for quick jigs vex.', i)}"
	)
	print(
	    f"wrap('The quick brown fox jumps over the lazy dog.', {i}) = {wrap('The quick brown fox jumps over the lazy dog.', i)}"
	)
	print(
	    f"wrap('Crazy Fredrick bought many very exquisite opal jewels.', {i}) = {wrap('Crazy Fredrick bought many very exquisite opal jewels.', i)}"
	)
	print(
	    f"wrap('The job requires extra pluck and zeal from every young wage earner.', {i}) = {wrap('The job requires extra pluck and zeal from every young wage earner.', i)}"
	)

	print()
