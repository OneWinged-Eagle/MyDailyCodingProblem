"""
Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
"""

from random import randrange
from typing import Set


def randomIntExclude(n: int, l: Set[int]) -> int:
	rands = [nb for nb in range(n) if nb not in l]

	return None if len(rands) == 0 else rands[randrange(len(rands))]


print(f"randomIntExclude(2, {{0, 1}}) = {randomIntExclude(2, {0, 1})}")

rands = [0] * 4
for i in range(10000):
	rands[randomIntExclude(6, {4, 5})] += 1
print(rands)
