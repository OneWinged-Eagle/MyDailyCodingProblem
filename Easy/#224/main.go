package main

/*
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.
*/

import "fmt"

func smallestSum(sorted []int) (sum int) {
	sum = 1
	if len(sorted) == 0 {
		return
	}

	for i := 0; i < len(sorted); i++ {
		if sorted[i] < 0 {
			continue
		}

		if sorted[i] > sum {
			return
		}
		sum += sorted[i]
	}

	return
}

func main() {
	fmt.Println("smallestSum([-2, -1, 0, 1, 2, 3, 10]) =", smallestSum([]int{-2, -1, 0, 1, 2, 3, 10}))
	fmt.Println("smallestSum([-2, -1, 0, 1, 2, 3, 7, 10]) =", smallestSum([]int{-2, -1, 0, 1, 2, 3, 7, 10}))
	fmt.Println("smallestSum([-2, -1, 0, 1, 2, 3, 7, 10, 24]) =", smallestSum([]int{-2, -1, 0, 1, 2, 3, 7, 10, 24}))
}
