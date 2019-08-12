"""
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""

def isPalindrome(string: str) -> bool:
	for i in range(len(string) // 2):
		if string[i] != string[len(string) - i - 1]:
			return False
	return True

def palindrome(string: str) -> str:
	if string in palindrome.cache:
		return palindrome.cache[string]

	if isPalindrome(string):
		palindrome.cache[string] = string
	elif string[0] == string[-1]:
		palindrome.cache[string] = string[0] + palindrome(string[1:-1]) + string[-1]
	else:
			pal1 = string[0] + palindrome(string[1:]) + string[0]
			pal2 = string[-1] + palindrome(string[:-1]) + string[-1]

			if len(pal1) == len(pal2):
				palindrome.cache[string] = pal1 if pal1 < pal2 else pal2
			else:
				palindrome.cache[string] = pal1 if len(pal1) < len(pal2) else pal2

	return palindrome.cache[string]

palindrome.cache = {}

print(f"palindrome('a') = {palindrome('a')}")
print(f"palindrome('aa') = {palindrome('aa')}")
print(f"palindrome('race') = {palindrome('race')}")
print(f"palindrome('google') = {palindrome('google')}")
print(f"palindrome('test') = {palindrome('test')}")
print(f"palindrome('tests') = {palindrome('tests')}")

print(f"cache = {palindrome.cache}")
