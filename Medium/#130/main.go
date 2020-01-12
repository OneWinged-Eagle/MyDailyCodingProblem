package main

/*
Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
*/

import (
	"fmt"
)

func max(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

func maxProfit(prices []int, k int) int {
	if len(prices) <= 1 || k <= 0 {
		return 0
	}

	profits := make([][]int, k+1)
	for i := range profits {
		profits[i] = make([]int, len(prices))
	}

	for i := 1; i <= k; i++ {
		diff := -prices[0]
		for j := 1; j < len(prices); j++ {
			profits[i][j] = max(profits[i][j-1], prices[j]+diff)
			diff = max(diff, profits[i-1][j]-prices[j])
		}
	}

	return profits[k][len(prices)-1]
}

func main() {
	fmt.Println("maxProfit([5, 2, 4, 0, 1], 2) =", maxProfit([]int{5, 2, 4, 0, 1}, 2))
}
