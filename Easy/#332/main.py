"""
Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following conditions:

    a + b = M
    a XOR b = N
"""


def nbGoodPairs(M: int, N: int) -> int:
	nb = 0

	for a in range(M // 2 + 1):
		b = M - a

		if a ^ b == N:
			nb += 1

	return nb


assert nbGoodPairs(-1, 1) == 0
assert nbGoodPairs(1, -1) == 0
assert nbGoodPairs(1, 1) == 1
print("passed")
