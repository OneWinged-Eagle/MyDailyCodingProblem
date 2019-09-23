"""
Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4

If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]

If a < c OR a==c AND b < d.
"""

from typing import Tuple

primes = [2]


def primeSum(nb: int) -> Tuple[int, int]:
	if nb <= 2 or nb % 2 != 0:
		return None

	for i in range(primes[-1] + 1, nb):
		if not any(i % prime == 0 for prime in primes):
			primes.append(i)

	for prime in primes:
		if nb - prime in primes:
			return (prime, nb - prime)

	return None


for nb in range(-2, 43, 2):
	print(f"primeSum({nb}) = {primeSum(nb)}")
