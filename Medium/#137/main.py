"""
Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

    init(size): initialize the array with size
    set(i, val): updates index at i with val where val is either 1 or 0.
    get(i): gets the value at index i
"""

from typing import List, Tuple

BIT_SIZE = 32


class BitArray():
	size: int
	length: int
	bitarray: List[int]

	def __init__(self, size: int):
		self.size = size
		self.length = (size // BIT_SIZE + (1 if size % BIT_SIZE > 0 else 0))
		self.bitarray = [0] * self.length

	def address(self, i: int) -> Tuple[int, int]:
		return (i // BIT_SIZE, i % BIT_SIZE)

	def set(self, i: int, val: bool) -> bool:
		if i < 0 or i >= self.size:
			return False

		n, b = self.address(i)

		if val:
			self.bitarray[n] = self.bitarray[n] | (1 << b)
		else:
			self.bitarray[n] = self.bitarray[n] & ~(1 << b)

		return True

	def get(self, i: int) -> bool:
		if i < 0 or i >= self.size:
			return False

		n, b = self.address(i)

		return (self.bitarray[n] & (1 << b)) != 0


b = BitArray(33)
assert not b.set(-1, 1)
assert b.set(0, 1)
assert b.set(32, 1)
assert not b.set(33, 1)

assert not b.get(-1)
assert b.get(0)
assert not b.get(16)
assert b.get(32)
assert not b.get(33)

print("passed")
