"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

openBrackets = {"(": 0, "{": 1, "[": 2}
closeBrackets = {")": 0, "}": 1, "]": 2}


def balancedBrackets(string: str) -> bool:
	balanced = []

	for char in string:
		if char in openBrackets:
			balanced.append(openBrackets.get(char))
		elif char in closeBrackets:
			if balanced[-1] != closeBrackets.get(char):
				return False
			balanced.pop()

	return len(balanced) == 0


print(f"balancedBrackets('([])[]({{}})') = {balancedBrackets('([])[]({})')}")
print(f"balancedBrackets('([)]') = {balancedBrackets('([)]')}")
print(f"balancedBrackets('((()') = {balancedBrackets('((()')}")
