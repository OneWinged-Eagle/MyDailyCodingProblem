"""
Given an integer n, find the next biggest integer with the same number of 1-bits on. For example, given the number 6 (0110 in binary), return 9 (1001).
"""


def nextSameBits(n: int) -> int:
	if n == 0:
		return 0

	rightBit = n & -n

	hightBit = n + rightBit

	rightBits = ((n ^ hightBit) // rightBit) >> 2

	return hightBit | rightBits


assert nextSameBits(0) == 0
assert nextSameBits(1) == 2
assert nextSameBits(2) == 4
assert nextSameBits(3) == 5
assert nextSameBits(4) == 8
assert nextSameBits(5) == 6
assert nextSameBits(6) == 9
assert nextSameBits(7) == 11
print('passed')
