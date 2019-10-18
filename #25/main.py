"""
Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
"""


# Doesn't work for lots of cases
def matchV1(string: str, regex: str) -> bool:
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
			if prevCn is None:
				return False
			elif prevCn == "." or prevCn == ci:
				i += 1
				if postCn is not None and postCi is not None and postCn == postCi:
					n += 1
			else:
				n += 1
		else:
			return False

	return True if i == len(string) and n == len(regex) else False


from typing import NamedTuple


class HelperArgs(NamedTuple):
	string: str
	regex: str
	lastChar: str


def helper(string: str, regex: str, lastChar: str) -> bool:
	if len(string) == 0 and len(regex) == 0:
		return True

	if len(string) == 0 or len(regex) == 0:
		return False

	helperArgs = HelperArgs(string, regex, lastChar)
	if helperArgs in helper.cache:
		return helper.cache[helperArgs]

	matched = False

	if string[0] == regex[0] or regex[0] == '.':
		matched |= helper(string[1:], regex[1:], regex[0])

	elif regex[0] == '*':
		if string[0] == lastChar or lastChar == '.':
			matched |= helper(string[1:], regex, lastChar) | \
                            helper(string[1:], regex[1:], regex[0])

		matched |= helper(string, regex[1:], regex[0])

	helper.cache[helperArgs] = matched
	return matched


helper.cache = {}


def match(string: str, regex: str) -> bool:
	return helper(string, regex, None)


print(f"match('ray', 'ra.') = {match('ray', 'ra.')}")
print(f"match('raymond', 'ra.*') = {match('raymond', 'ra.*')}")
print(f"match('raymond', 'ra.') = {match('raymond', 'ra.')}")

print(f"match('chat', '.*at') = {match('chat', '.*at')}")
print(f"match('chats', '.*ats') = {match('chats', '.*ats')}")
print(f"match('chats', '.*at') = {match('chats', '.*at')}")

print(
    f"match('what where when', '.* where .*') = {match('what where when', '.* where .*')}"
)
print(
    f"match('what where when', '.*where.*') = {match('what where when', '.*where.*')}"
)
print(
    f"match('whatwherewhen', '.* where .*') = {match('whatwherewhen', '.* where .*')}"
)

print(f"match('aaaaaaaaaaaa', 'a*') = {match('aaaaaaaaaaaa', 'a*')}")
print(f"match('aaaaaaaaaaaab', 'a*b') = {match('aaaaaaaaaaaab', 'a*b')}")
print(f"match('aaaaaaaaaaaab', 'a*') = {match('aaaaaaaaaaaab', 'a*')}")

print(helper.cache)
