"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


# time O(n²), space O(n²)
def bruteForce(s: str, k: int) -> str:
	length = len(s)
	substrings = []

	for i in range(length):
		for j in range(i + 1, length + 1):
			substring = s[i:j]
			if len(set(substring)) <= k:
				substrings.append(substring)

	return max(substrings, key=len)


# time O(n), space O(1) (O(n) maybe?)
def longestSubstring(s: str, k: int) -> str:
	length = len(s)
	longestSubstring = ""
	substring = ""
	start = 0

	for end in range(1, length + 1):
		substring = s[start:end]

		while len(set(substring)) > k:
			start += 1
			substring = s[start:end]

		if len(substring) > len(longestSubstring):
			longestSubstring = substring

	return longestSubstring


substr1 = longestSubstring("abcba", 2)
print(f"longestSubstring(\"abcba\", 2) = {substr1}")
substr2 = longestSubstring("abcba", 3)
print(f"longestSubstring(\"abcba\", 3) = {substr2}")
