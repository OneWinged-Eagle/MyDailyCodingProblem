"""
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
"""


def permPalindrome(string: str) -> bool:
	s = set()

	for c in string:
		if c in s:
			s.remove(c)
		else:
			s.add(c)

	if len(string) % 2 == 1 and len(s) == 1:
		return True

	if len(string) % 2 == 0 and len(s) == 0:
		return True

	return False


assert permPalindrome("carrace")
assert permPalindrome("carrac")
assert not permPalindrome("carrade")
assert not permPalindrome("carrae")
print("passed")
