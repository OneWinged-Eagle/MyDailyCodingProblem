"""
Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
"""


def match(string: str, regex: str) -> bool:
	i, n = 0, 0
	while i < len(string) and n < len(regex):
		ci = string[i]
		cn = regex[n]

		if cn == "." or cn == ci:
			i += 1
			n += 1
		elif cn == "*":
			prevCn = None if n - 1 < 0 else regex[n - 1]
			postCn = None if n + 1 >= len(regex) else regex[n + 1]
			postCi = None if i + 1 >= len(string) else string[i + 1]
			if prevCn == None:
				return False
			elif prevCn == "." or prevCn == ci:
				i += 1
				if postCn != None and postCi != None and postCn == postCi:
					n += 1
			else:
				n += 1
		else:
			return False

	return True if i == len(string) and n == len(regex) else False


print(f"match('ray', 'ra.') = {match('ray', 'ra.')}")
print(f"match('raymond', 'ra.') = {match('raymond', 'ra.')}")

print(f"match('chat', '.*at') = {match('chat', '.*at')}")
print(f"match('chats', '.*at') = {match('chats', '.*at')}")
