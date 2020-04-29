"""
UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.

For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100. The rules for mapping characters are as follows:

    For a single-byte character, the first bit must be zero.
    For an n-byte character, the first byte starts with n ones and a zero. The other n - 1 bytes all start with 10.

Visually, this can be represented as follows.

 Bytes   |           Byte format
-----------------------------------------------
   1     | 0xxxxxxx
   2     | 110xxxxx 10xxxxxx
   3     | 1110xxxx 10xxxxxx 10xxxxxx
   4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Write a program that takes in an array of integers representing byte values, and returns whether it is a valid UTF-8 encoding.
"""

from typing import List


def isUTF8(bits: List[bool]) -> bool:
	if len(bits) % 8 != 0:
		return False

	nbBytes = len(bits) // 8

	if nbBytes == 1:
		return not bits[0]

	if bits[0:nbBytes + 1] != [True] * nbBytes + [False]:
		return False

	for n in range(1, nbBytes):
		if bits[n * 8:n * 8 + 2] != [True, False]:
			return False

	return True


assert isUTF8([False, True, True, True, True, True, True, True])
assert not isUTF8([True, True, True, True, True, True, True, True])

assert isUTF8([
    True, True, False, True, True, True, True, True, True, False, True, True,
    True, True, True, True
])
assert not isUTF8([
    True, True, True, False, True, True, True, True, True, False, True, True,
    True, True, True, True
])
assert not isUTF8([
    True, True, False, True, True, True, True, True, True, True, True, True,
    True, True, True, True
])

assert isUTF8([
    True, True, True, False, True, True, True, True, True, False, True, True,
    True, True, True, True, True, False, True, True, True, True, True, True
])

assert isUTF8([
    True, True, True, True, False, True, True, True, True, False, True, True,
    True, True, True, True, True, False, True, True, True, True, True, True,
    True, False, True, True, True, True, True, True
])

print("passed")
