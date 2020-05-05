"""
On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file.
Write a program that reads this file as a stream and returns the top 3 candidates at any given time.
If you find a voter voting more than once, report this as fraud.
"""

from typing import List, Tuple
from bisect import insort


def votes(votes: List[Tuple[int, int]]) -> Tuple[int, int, int]:
	candidates = dict()
	s = set()

	for voter, candidate in votes:
		if voter in s:
			return (voter, -1, -1)
		s.add(voter)
		candidates[candidate] = candidates.get(candidate, 0) + 1

	podium = [
	    c for c, v in sorted(candidates.items(), key=lambda item: item[1])[:3]
	]
	while len(podium) < 3:
		podium = [0] + podium
	return (podium[2], podium[1], podium[0])


assert votes([(1, 1), (1, 2)]) == (1, -1, -1)
assert votes([(1, 1), (2, 2), (3, 3), (4, 1), (5, 2), (6, 1)]) == (1, 2, 3)
assert votes([(1, 1), (2, 2), (4, 1), (5, 2), (6, 1)]) == (1, 2, 0)
print("passed")
