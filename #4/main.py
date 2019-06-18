# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.


# time O(n), space O(n)
def missingIntegerWithSpaceN(numbers):
	s = set(numbers)
	i = 1

	while True:
		if i not in s:
			return i
		i += 1


# time O(n), space O(1)
def rearrange(numbers):
	nbPositives = 0
	for i, nb in enumerate(numbers):
		if nb > 0:
			numbers[i], numbers[nbPositives] = numbers[nbPositives], numbers[i]
			nbPositives += 1
	return nbPositives


# time O(n), space O(1)
def missingInteger(numbers):
	end = rearrange(numbers)
	for i, nb in enumerate(numbers[:end]):
		x = abs(nb)
		if x <= end:
			numbers[x - 1] = -abs(numbers[x - 1])

	for i, nb in enumerate(numbers[:end]):
		if nb > 0:
			return i + 1

	return end + 1


print(f"missingInteger([1, 2, 3, 4, 5]) = {missingInteger([1, 2, 3, 4, 5])}")

print(f"missingInteger([3, -2, 1]) = {missingInteger([3, -2, 1])}")

print(f"missingInteger([1, 2, 0, 4, 5]) = {missingInteger([1, 2, 0, 4, 5])}")

print(f"missingInteger([1, 0, 3, 0, 5]) = {missingInteger([1, 0, 3, 0, 5])}")
