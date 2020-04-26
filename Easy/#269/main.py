"""
You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:

    L, meaning the domino has just been pushed to the left,
    R, meaning the domino has just been pushed to the right, or
    ., meaning the domino is standing still.

Determine the orientation of each tile when the dominoes stop falling. Note that if a domino receives a force from the left and right side simultaneously, it will remain upright.

For example, given the string .L.R....L, you should return LL.RRRLLL.

Given the string ..R...L.L, you should return ..RR.LLLL.
"""


def falling(dominoes: str) -> str:
	tracked = list()

	for i, char in enumerate(dominoes):
		if char == 'L' or char == 'R':
			tracked.append((i, char))
		elif char != '.':
			return f"String \"{dominoes}\" badly formatted"

	result = ""
	start = -1
	tilt = 'L'
	for i, char in tracked:
		length = (i - start) + 1

		if char == tilt:
			result += (length - 1) * char
			start = i
		else:
			if char == 'R':
				result += (length - 2) * '.'
			elif char == 'L':
				result += length // 2 * 'R'
				if length % 2 != 0:
					result += '.'
				result += length // 2 * 'L'
			start = i
			tilt = char

	if tilt == 'R':
		while start < len(dominoes):
			result += 'R'

	return result


assert falling(".L.R....L") == "LL.RRRLLL"
assert falling("..R...L.L") == "..RR.LLLL"
print("passed")
