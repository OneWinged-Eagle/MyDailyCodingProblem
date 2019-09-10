"""
Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.
"""

from typing import Tuple


def division(dividend: int, divisor: int) -> Tuple[int, int]:
	if divisor == 0:
		return None

	sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

	dividend, divisor, quotient = abs(dividend), abs(divisor), 0

	while dividend >= divisor:
		dividend -= divisor
		quotient += 1

	return sign * quotient, dividend


print(f"division(10, 5) = {division(10, 5)}")
print(f"division(10, -3) = {division(10, -3)}")
print(f"division(-10, -2) = {division(-10, -2)}")
print(f"division(10, 10) = {division(10, 10)}")
print(f"division(10, 20) = {division(10, 20)}")
print(f"division(10, 0) = {division(10, 0)}")
