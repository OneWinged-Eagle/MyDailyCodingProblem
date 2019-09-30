"""
Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""


def shiftableV1(A: str, B: str) -> bool:
	if len(A) != len(B):
		return False

	for i, char in enumerate(A):
		if char == B[0] and A[i:] + A[:i] == B:
			return True

	return False


def shiftable(A: str, B: str) -> bool:
	if len(A) != len(B):
		return False

	if (A + A).find(B) != -1:
		return True

	return False


print(f"shiftable('abcde', 'cdeab') = {shiftable('abcde', 'cdeab')}")
print(f"shiftable('abc', 'acb') = {shiftable('abc', 'acb')}")
