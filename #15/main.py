"""
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""

from random import randrange
from typing import Any, Iterable, List


# with n = len(stream): time O(n), space O(k)
def reservoirSampling(stream: Iterable[Any], k: int) -> List[Any]:
	reservoir = []
	for i, e in enumerate(stream):
		if i < k:
			reservoir.append(e)
		else:
			r = randrange(i + 1)
			if r < k:
				reservoir[r] = e

	return reservoir


# time O(1), space O(1), but uses len(stream)
def pickOne(stream: Iterable[Any]) -> Any:
	return stream[randrange(len(stream))]


print(f"pickOne([2, 4, 6, 8, 10]) = {reservoirSampling([2, 4, 6, 8, 10], 1)}")
print(f"pickOne([2, 4, 6, 8, 10]) = {reservoirSampling([2, 4, 6, 8, 10], 1)}")
print(f"pickOne([2, 4, 6, 8, 10]) = {reservoirSampling([2, 4, 6, 8, 10], 1)}")
print(f"pickOne([2, 4, 6, 8, 10]) = {reservoirSampling([2, 4, 6, 8, 10], 1)}")
print(f"pickOne([2, 4, 6, 8, 10]) = {reservoirSampling([2, 4, 6, 8, 10], 1)}")

print(f"pickOne([2, 4, 6, 8, 10]) = {pickOne([2, 4, 6, 8, 10])}")
print(f"pickOne([2, 4, 6, 8, 10]) = {pickOne([2, 4, 6, 8, 10])}")
print(f"pickOne([2, 4, 6, 8, 10]) = {pickOne([2, 4, 6, 8, 10])}")
print(f"pickOne([2, 4, 6, 8, 10]) = {pickOne([2, 4, 6, 8, 10])}")
print(f"pickOne([2, 4, 6, 8, 10]) = {pickOne([2, 4, 6, 8, 10])}")
