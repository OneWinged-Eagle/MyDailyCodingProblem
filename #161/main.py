"""
Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 1111 1111 1111 1111 1111 1111 1111, return 1111 1111 1111 1111 1111 1111 1111 1111
"""

SET_32BIT = 0b11111111111111111111111111111111


def reverse(nb: int) -> int:
	return nb ^ SET_32BIT


print(f"reverse({bin(42)}) = {bin(reverse(42))}")
