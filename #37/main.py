"""
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

from typing import Any, List, Set

def powerSet(s: Set[Any]) -> Set[Set[Any]]:
	subSets = {frozenset()}
	for key in s:
		subSets = subSets|{subSet|{key} for subSet in subSets}
	return subSets

print(f"powerSet({{1, 2, 3}}) = {powerSet({1, 2, 3})}")
print(f"powerSet({{'T', 'e', 's', 't'}}) = {powerSet({'T', 'e', 's', 't'})}")
