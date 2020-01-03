"""
Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.
"""

from typing import List

# with n = len(exchanges), Time O(n²), Space O(1)
def arbitrage(exchanges: List[List[float]]) -> bool:
	if exchanges[0][0] > 1:
		return True

	for i, row in enumerate(exchanges[1:]):
		for n, rate in enumerate(row):
			if rate > exchanges[0][n] / exchanges[0][i + 1]:
				return True

	return False

exchanges = [[1, 2, 3], [0.5, 1, 1.5], [1/3, 2/3, 1]]
print(f"arbitrage({exchanges}) = {arbitrage(exchanges)}")

exchanges[1][2] = 1.4
print(f"arbitrage({exchanges}) = {arbitrage(exchanges)}")

exchanges[1][2] = 1.6
print(f"arbitrage({exchanges}) = {arbitrage(exchanges)}")
