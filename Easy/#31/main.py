"""
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

from typing import NamedTuple


class DistanceArgs(NamedTuple):
	str1: int
	str2: str


# with n = min(len(str1), len(str2)), Time O(n), Space O(1)  —  Too naive?
def distanceV1(str1: str, str2: str) -> int:
	distance = abs(len(str1) - len(str2))

	for c1, c2 in zip(str1, str2):
		if c1 != c2:
			distance += 1

	return distance

# with n1 = len(str1) and n2 = len(str2), Time O(n1 * n2), Space O(n1 * n2)
def distance(str1: str, str2: str) -> int:
	distanceArgs = DistanceArgs(str1, str2)
	if distanceArgs in distance.cache:
		return distance.cache[distanceArgs]

	if len(str1) == 0 or len(str2) == 0:
		distance.cache[distanceArgs] = len(str1) + len(str2)
	elif str1[-1] == str2[-1]:
		distance.cache[distanceArgs] = distance(str1[:-1], str2[:-1])
	else:
		distance.cache[distanceArgs] = 1 + min(distance(str1[:-1], str2), distance(str1, str2[:-1]), distance(str1[:-1], str2[:-1]))

	return distance.cache[distanceArgs]

distance.cache = {}

print(f"distance('kitten', 'sitting') = {distance('kitten', 'sitting')}")
print(f"distance('surf', 'suliporf') = {distance('surf', 'suliporf')}")
print(
    f"distance('what', 'when what where') = {distance('what', 'when what where')}"
)
