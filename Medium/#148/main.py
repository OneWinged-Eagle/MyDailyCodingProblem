"""
Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around. Gray code is common in hardware so that we don't see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].
"""

from typing import List


def grayCode(n: int) -> List[int]:
	if n <= 0:
		return []

	code = [0]

	while not (code[-1] & (1 << (n - 1))):
		code.append(code[-1] | code[-1] + 1)

	if n > 1:
		while code[-1] & (1 << (n - 2)):
			code.append(code[-1] & code[-1] - 1)

	return code


for n in range(5):
	print(f"grayCode({n}) = {[bin(i) for i in grayCode(n)]}")
