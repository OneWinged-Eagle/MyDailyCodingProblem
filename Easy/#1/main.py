"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


# time O(n²), space O(1), don't check if nb1 and nb2 are strictly the same
def bruteForce(numbers, k):
	for nb in numbers:
		if k - nb in numbers:
			return True
	return False


# time O(n), space O(n)
def addUpTo(numbers, k):
	s = set()

	for nb in numbers:
		if k - nb in s:
			return True
		s.add(nb)
	return False


print(f"addUpTo([10, 15, 3, 7], 17) = {addUpTo([10, 15, 3, 7], 17)}")

print(f"addUpTo([10, 15, 3, 7], 16) = {addUpTo([10, 15, 3, 7], 16)}")

print(
    f"addUpTo([10, 15, 3, 7, 20, -3], 17) = {addUpTo([10, 15, 3, 7, 20, -3], 17)}"
)

print(
    f"addUpTo([10, 15, 3, 7, 20, -3], 20) = {addUpTo([10, 15, 3, 7, 20, -3], 20)}"
)
