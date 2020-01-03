package main

/*
Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
*/

import "fmt"

type void struct{}

func max(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

func lenDistincts(numbers []int) (maxLen int) {
	if len(numbers) == 0 {
		return
	}

	start, end := 0, 1
	set := make(map[int]void)
	set[numbers[0]] = void{}

	for start < len(numbers) && end < len(numbers) {
		if _, exists := set[numbers[end]]; exists {
			maxLen = max(maxLen, end-start)
			delete(set, numbers[start])
			start++
		} else {
			set[numbers[end]] = void{}
			end++
		}
	}

	return max(maxLen, end-start)
}

func main() {
	array := []int{5, 1, 3, 5, 2, 3, 4, 1}
	fmt.Printf("lenDistincts(%v) = %v\n", array, lenDistincts(array))

	array = []int{5, 1, 3, 5, 2, 3, 2, 1}
	fmt.Printf("lenDistincts(%v) = %v\n", array, lenDistincts(array))

	array = []int{5, 5, 5, 5, 2, 3, 4, 1}
	fmt.Printf("lenDistincts(%v) = %v\n", array, lenDistincts(array))

	array = []int{5, 5, 3, 5, 2, 3, 2, 1}
	fmt.Printf("lenDistincts(%v) = %v\n", array, lenDistincts(array))

	array = []int{5, 5, 5, 5, 2, 3, 5, 5}
	fmt.Printf("lenDistincts(%v) = %v\n", array, lenDistincts(array))
}
