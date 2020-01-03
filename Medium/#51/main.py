"""
Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""

from random import randint
from typing import Any, List


def randK(k: int) -> int:
	return randint(1, k)


def shuffle(arr: List[Any]) -> None:
	for i in range(len(arr)):
		rand = randK(i + 1) - 1
		arr[i], arr[rand] = arr[rand], arr[i]


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(arr)
print(f"[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] after first shuffle = {arr}")
shuffle(arr)
print(f"[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] after second shuffle = {arr}")
shuffle(arr)
print(f"[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] after third shuffle = {arr}")
