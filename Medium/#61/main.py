"""
Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""


def pow(x: int, y: int) -> int:
	if y == 0:
		return 1

	half = pow(x, y // 2)

	if y % 2 == 0:
		return half * half
	elif y > 0:
		return x * half * half
	else:
		return (half * half) / x


for i in range(25):
	print(f"pow(2, {i}) = {pow(2, i)}")
