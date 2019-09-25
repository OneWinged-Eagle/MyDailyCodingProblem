"""
Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""

from typing import Set


def substring(string: str, chars: Set[str]) -> str:
	substr = None
	start, end = 0, 0
	checks = dict()

	while start < len(string):
		if len(checks) == len(chars):
			if substr == None or end - start < len(substr):
				substr = string[start:end]

			if string[start] in checks:
				checks[string[start]] -= 1
				if checks[string[start]] == 0:
					del checks[string[start]]

			start += 1

		elif end < len(string):
			if string[end] in chars:
				checks[string[end]] = checks.get(string[end], 0) + 1

			end += 1

		elif end == len(string):
			start += 1

	return substr


print(
    f"substring('figehaeci', {'a', 'e', 'i'}) = {substring('figehaeci', {'a', 'e', 'i'})}"
)

print(
    f"substring('figehaeciae', {'a', 'e', 'i'}) = {substring('figehaeciae', {'a', 'e', 'i'})}"
)

print(
    f"substring('figehaeci', {'a', 'e', 'i', 'k'}) = {substring('figehaeci', {'a', 'e', 'i', 'k'})}"
)

print(f"substring('', {'a', 'e', 'i'}) = {substring('', {'a', 'e', 'i'})}")

print(
    f"substring('ujioklredscvbiorfedgfouiretuiogvhtuofrd', {'o', 'f'}) = {substring('ujioklredscvbiorfedgfouiretuiogvhtuofrd', {'o', 'f'})}"
)
