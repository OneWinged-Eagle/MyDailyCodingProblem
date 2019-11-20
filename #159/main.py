"""
Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""


def firstRec(string: str) -> str:
	s = set()

	for c in string:
		if c in s:
			return c
		else:
			s.add(c)

	return None


assert firstRec("acbbac") == 'b'
assert firstRec("abcdef") == None
print("passed")
