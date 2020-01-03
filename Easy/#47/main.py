"""
Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars
"""

from typing import List


def maxProfit(prices: List[int]) -> int:
	if len(prices) < 2:
		return 0

	minPrice, profit = prices[0], 0

	for price in prices[1:]:
		if price < minPrice:
			minPrice = price
		elif price - minPrice > profit:
			profit = price - minPrice

	return profit


print(f"maxProfit([9, 11, 8, 5, 7, 10]) = {maxProfit([9, 11, 8, 5, 7, 10])}")
print(f"maxProfit([9, 11]) = {maxProfit([9, 11])}")
print(f"maxProfit([9]) = {maxProfit([9])}")
print(
    f"maxProfit([50, 101, 120, 166, 27, 222, 287]) = {maxProfit([50, 101, 120, 166, 27, 222, 287])}"
)
print(
    f"maxProfit([40, 3, 48, 651, -1, 448, 645, -10]) = {maxProfit([40, 3, 48, 651, -1, 448, 645, -10])}"
)
