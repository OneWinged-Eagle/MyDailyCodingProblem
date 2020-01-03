"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


# time O(n) (??? I really have a hard time telling the time complexity for recursives...), space O(n)
def nb_ways(encoded):
	if len(encoded) == 0:
		return 1

	if encoded[0] == "0":
		return 0

	if encoded[1:] not in nb_ways.cache:
		nb_ways.cache[encoded[1:]] = nb_ways(encoded[1:])

	if len(encoded) >= 2 and "10" <= encoded[:2] <= "26":
		if encoded[2:] not in nb_ways.cache:
			nb_ways.cache[encoded[2:]] = nb_ways(encoded[2:])
		return nb_ways.cache[encoded[1:]] + nb_ways.cache[encoded[2:]]

	return nb_ways.cache[encoded[1:]]


nb_ways.cache = {}

ways111 = nb_ways("111")
print(f"nb_ways(\"111\") = {ways111}")

ways262026 = nb_ways("262026")
print(f"nb_ways(\"262026\") = {ways262026}")

ways262126 = nb_ways("262126")
print(f"nb_ways(\"262126\") = {ways262126}")

ways362136 = nb_ways("362136")
print(f"nb_ways(\"362136\") = {ways362136}")

ways362136362136 = nb_ways("362136362136")
print(f"nb_ways(\"362136362136\") = {ways362136362136}")

ways362136362136362136 = nb_ways("362136362136362136")
print(f"nb_ways(\"362136362136362136\") = {ways362136362136362136}")

ways362936362936362936 = nb_ways("362936362936362936")
print(f"nb_ways(\"362936362936362936\") = {ways362936362936362936}")

ways1111 = nb_ways("1111")
print(f"nb_ways(\"1111\") = {ways1111}")

ways2222 = nb_ways("2222")
print(f"nb_ways(\"2222\") = {ways2222}")

ways123450123541023541201 = nb_ways("123450123541023541201")
print(f"nb_ways(\"123450123541023541201\") = {ways123450123541023541201}")

ways12345201235410235412010 = nb_ways("12345201235410235412010")
print(f"nb_ways(\"12345201235410235412010\") = {ways12345201235410235412010}")

print(nb_ways.cache)
