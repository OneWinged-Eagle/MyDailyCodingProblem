"""
Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""

coins = [25, 10, 5, 1]


def nbCoins(n: int) -> int:
	if n < 0:
		return None

	nb = 0

	for coin in coins:
		nb += n // coin
		n %= coin

	return nb


assert nbCoins(-1) == None
assert nbCoins(0) == 0
assert nbCoins(1) == 1
assert nbCoins(5) == 1
assert nbCoins(6) == 2
assert nbCoins(10) == 1
assert nbCoins(11) == 2
assert nbCoins(15) == 2
assert nbCoins(16) == 3
assert nbCoins(25) == 1
assert nbCoins(26) == 2
assert nbCoins(30) == 2
assert nbCoins(31) == 3
assert nbCoins(35) == 2
assert nbCoins(36) == 3
assert nbCoins(40) == 3
assert nbCoins(41) == 4
print("passed")
