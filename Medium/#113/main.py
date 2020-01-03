"""
Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?
"""


def reverse(string: str) -> str:
	return " ".join(reversed(string.split(" ")))


print(f"reverse('hello world here') = {reverse('hello world here')}")
