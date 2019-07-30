"""
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
"""

import numpy as np


def isPalindrome(string: str) -> bool:
	for i in range(len(string) // 2):
		if string[i] != string[len(string) - i - 1]:
			return False
	return True


# with n = len(string), Time O(n³), Space O(1)
def longestPalindromeV1(string: str) -> str:
	palindrome = ""

	for i in range(len(string)):
		for j in range(i, len(string)):
			if isPalindrome(string[i:j + 1]) and j + 1 - i > len(palindrome):
				palindrome = string[i:j + 1]

	return palindrome


# with n = len(string), Time O(n²), Space O(n²)
def longestPalindrome(string: str) -> str:
	if not string:
		return ""

	palindrome = string[0]

	tableIsPalindrome = np.identity(len(string), bool)

	for length in range(2, len(string) + 1):
		for i in range(len(string) - length + 1):
			j = i + length - 1

			if (length == 2 or
			    tableIsPalindrome[i + 1][j - 1]) and string[i] == string[j]:
				tableIsPalindrome[i][j] = True

				if length > len(palindrome):
					palindrome = string[i:j + 1]

	return palindrome


print(f"longestPalindrome('aabcdcb') = {longestPalindrome('aabcdcb')}")
print(f"longestPalindrome('bananas') = {longestPalindrome('bananas')}")
print(f"longestPalindrome('testset') = {longestPalindrome('testset')}")
print(f"longestPalindrome('test') = {longestPalindrome('test')}")
print(f"longestPalindrome('') = {longestPalindrome('')}")
print(f"longestPalindrome('hummuh') = {longestPalindrome('hummuh')}")
print(f"longestPalindrome('hummhu') = {longestPalindrome('hummhu')}")
