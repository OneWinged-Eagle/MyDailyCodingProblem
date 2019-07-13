"""
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""


# with n = len(string), time O(n), space O(n)
def encoding(string: str) -> str:
	encoded = ""

	count = 0
	lastChar = ""
	for char in string:
		if char == lastChar:
			count += 1
		else:
			if count != 0:
				encoded += f"{count}{lastChar}"
			count = 1
			lastChar = char

	if count != 0:
		encoded += f"{count}{lastChar}"

	return encoded


# with n = len(encoded), time O(n), space O(n)
def decoding(encoded: str) -> str:
	decoded = ""

	count = 0
	for char in encoded:
		if "0" <= char <= "9":
			count = count * 10 + int(char)
		else:
			decoded += char * count
			count = 0

	return decoded


string = "$$$$$AAAA**********BBB;;CC'''D__AA("
encoded = encoding(string)
print(f"encoding(\"{string}\") = {encoded}")
decoded = decoding(encoded)
print(f"decoding(\"{encoded}\") = {decoded}")
print(f"string == decoded ? {string == decoded}")
