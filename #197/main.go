package main

/*
Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.
*/

import "fmt"

func rotateRight(array []int, k int) []int {
	if len(array) <= 1 {
		return array
	}

	k = k % len(array)

	if k <= 0 {
		return array
	}

	ret := array[0]
	for step, i := 0, k; step < len(array); step, i = step+1, (i+k)%len(array) {
		ret, array[i] = array[i], ret
	}

	return array
}

func main() {
	for k := -1; k <= 6; k++ {
		fmt.Printf("rotateRight([1, 2, 3, 4, 5], %d) = %v\n", k, rotateRight([]int{1, 2, 3, 4, 5}, k))
	}
}
