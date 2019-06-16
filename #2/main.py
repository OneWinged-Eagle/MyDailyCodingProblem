# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?


# time O(n), space O(n)
def products(numbers):
	products = [0] * len(numbers)
	prod = 1
	zeroIndex = -1

	for i, nb in enumerate(numbers):
		if nb == 0:
			if zeroIndex == -1:
				zeroIndex = i
			else:
				return products
		else:
			prod *= nb

	if zeroIndex != -1:
		products[zeroIndex] = prod
	else:
		for i, nb in enumerate(numbers):
			products[i] = int(prod * nb**-1)

	return products


print(f"products([1, 2, 3, 4, 5]) = {products([1, 2, 3, 4, 5])}")

print(f"products([3, -2, 1]) = {products([3, -2, 1])}")

print(f"products([1, 2, 0, 4, 5]) = {products([1, 2, 0, 4, 5])}")

print(f"products([1, 0, 3, 0, 5]) = {products([1, 0, 3, 0, 5])}")
