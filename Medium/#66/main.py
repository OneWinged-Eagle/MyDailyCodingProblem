"""
This problem was asked by Square.

Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
"""

from random import random


def toss_biased(p: int = 0.2) -> bool:
	return True if random() < p else False


def unbiased() -> bool:
	couple = toss_biased(), toss_biased()

	if couple[0] and not couple[1]:
		return True

	if not couple[0] and couple[1]:
		return False

	return unbiased()


trues, falses = 0, 0

for i in range(1000000):
	if unbiased():
		trues += 1
	else:
		falses += 1

print(f"trues = {trues}, false = {falses}")
