package main

/*
Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
*/

import "fmt"

func max(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

func maxSubarray(numbers []int) (maxSum int) {
	if len(numbers) == 0 {
		return
	}

	start := 0
	for start < len(numbers) && numbers[start] >= 0 {
		start++
	}

	i := start + 1
	if i == len(numbers) {
		i = 0
	}

	sum := 0
	for i != start {
		if numbers[i] < 0 {
			maxSum, sum = max(maxSum, sum), 0
		} else {
			sum += numbers[i]
		}

		i++
		if i == len(numbers) {
			i = 0
		}
	}

	return max(maxSum, sum)
}

func main() {
	fmt.Println("maxSubarray([8, -1, 3, 4]) =", maxSubarray([]int{8, -1, 3, 4}))
	fmt.Println("maxSubarray([-4, 5, 1, 0]) =", maxSubarray([]int{-4, 5, 1, 0}))
}
