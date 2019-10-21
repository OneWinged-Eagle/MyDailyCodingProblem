"""
Given a real number n, find the square root of n. For example, given n = 9, return 3.
"""


def sqrt(n: int) -> int:
	if n < 0:
		return None

	if n <= 1:
		return n

	start, end = 1, n // 2
	root = 1

	while start <= end:
		mid = (start + end) // 2
		squared = mid**2

		if squared < n:
			start = mid + 1
			root = mid
		elif squared > n:
			end = mid - 1
		else:
			return mid

	return root


for n in range(21):
	print(f"sqrt({n}) = {sqrt(n)}")
