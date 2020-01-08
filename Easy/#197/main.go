package main

/*
Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.
*/

import "fmt"

func gcd(a int, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func rotateRight(array []int, k int) []int {
	if len(array) <= 1 {
		return array
	}

	k = k % len(array)

	if k <= 0 {
		return array
	}

	for i := 0; i < gcd(k, len(array)); i++ {
		for j := (i + k) % len(array); j != i; j = (j + k) % len(array) {
			array[i], array[j] = array[j], array[i]
		}
	}

	return array
}

func main() {
	for k := -1; k <= 6; k++ {
		fmt.Printf("rotateRight([1, 2, 3, 4, 5], %d) = %v\n", k, rotateRight([]int{1, 2, 3, 4, 5}, k))
	}

	for k := -1; k <= 7; k++ {
		fmt.Printf("rotateRight([1, 2, 3, 4, 5, 6], %d) = %v\n", k, rotateRight([]int{1, 2, 3, 4, 5, 6}, k))
	}
}
