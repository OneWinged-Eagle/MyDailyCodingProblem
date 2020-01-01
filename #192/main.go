package main

/*
You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying to advance to the end. You can advance at most, the number of steps that you're currently on. Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
*/

import "fmt"

func max(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

func canReachEnd(steps []int) bool {
	i, lastIndex := 0, len(steps)-1

	for s := steps[i]; i < lastIndex && s > 0; s = max(s-1, steps[i]) {
		i++
	}

	return i == lastIndex
}

func main() {
	fmt.Println("canReachEnd([1, 3, 1, 2, 0, 1]) = ", canReachEnd([]int{1, 3, 1, 2, 0, 1}))
	fmt.Println("canReachEnd([1, 2, 1, 0, 0]) = ", canReachEnd([]int{1, 2, 1, 0, 0}))
}
