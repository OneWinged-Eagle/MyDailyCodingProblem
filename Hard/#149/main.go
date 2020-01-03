package main

/*
Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.
*/

import "fmt"

func sum(array []int) (s int) {
	for _, nb := range array {
		s += nb
	}
	return
}

type preSum struct {
	sums []int
}

func newPreSum(array []int) *preSum {
	sums := make([]int, len(array)+1)
	for i, nb := range array {
		sums[i+1] = sums[i] + nb
	}

	return &preSum{sums}
}

func (ps preSum) sum(i, j int) int {
	if i >= j || i < 0 || j >= len(ps.sums) {
		return 0
	}

	return ps.sums[j] - ps.sums[i]
}

func main() {
	array := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
	presum := newPreSum(array)

	for i := range array {
		for j := i + 1; j <= len(array); j++ {
			fmt.Printf("presum.sum(%d, %d) = %d (%d)\n", i, j, presum.sum(i, j), sum(array[i:j]))
		}
	}

	print("\n")

	array = []int{-2, 4, 8, -9, 10, 22, -42, -50, 200}
	presum = newPreSum(array)

	for i := range array {
		for j := i + 1; j <= len(array); j++ {
			fmt.Printf("presum.sum(%d, %d) = %d (%d)\n", i, j, presum.sum(i, j), sum(array[i:j]))
		}
	}
}
