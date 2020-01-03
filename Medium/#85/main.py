"""
Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0
"""


def xy(x: int, y: int, b: int) -> int:
	if b != 0 and b != 1:
		return None

	return b * x + (b ^ 1) * y


print(f"xy(42, -10, 1) = {xy(42, -10, 1)}")
print(f"xy(-10, 42, 0) = {xy(-10, 42, 0)}")
