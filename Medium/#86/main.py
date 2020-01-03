"""
Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.
"""


def rmParentheses(string: str) -> int:
	if not string or len(string) == 0:
		return -1

	left, right = 0, 0

	for char in string:
		if char == '(':
			left += 1
		elif char == ')':
			if left > 0:
				left -= 1
			else:
				right += 1
		else:
			return -1

	return left + right


print(f"rmParentheses('()())()') = {rmParentheses('()())()')}")
print(f"rmParentheses(')(') = {rmParentheses(')(')}")
print(f"rmParentheses(')()((') = {rmParentheses(')()((')}")
print(f"rmParentheses('))(()()(') = {rmParentheses('))(()()(')}")
