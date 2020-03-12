package main

/*
Given an array of integers out of order, determine the bounds of the smallest window that must be sorted in order for the entire array to be sorted. For example, given [3, 7, 5, 6, 9], you should return (1, 3).
*/

import "fmt"

func sortBounds(array []int) (bounds [2]uint) {
	if len(array) == 0 {
		return
	}

	i, max := 0, array[0]

	for ; i < len(array)-1; i++ {
		if max < array[i] {
			max = array[i]
		}

		if array[i] > array[i+1] {
			bounds[0] = uint(i)
			break
		}
	}

	if i == len(array)-1 {
		return [2]uint{0, 0}
	}

	for ; i < len(array) && array[i] <= max; i++ {
	}

	bounds[1] = uint(i - 1)

	for ; i < len(array)-1; i++ {
		if array[i] < array[i+1] {
			bounds[1] = uint(i - 1)
		}
	}

	return
}

func main() {
	array := []int{3, 7, 5, 6, 9}
	fmt.Printf("sortBounds(%v) = %v\n", array, sortBounds(array))

	array = []int{3, 5, 6, 7, 9}
	fmt.Printf("sortBounds(%v) = %v\n", array, sortBounds(array))

	array = []int{9, 7, 6, 5, 3}
	fmt.Printf("sortBounds(%v) = %v\n", array, sortBounds(array))

	array = []int{7, 6, 5, 3, 9}
	fmt.Printf("sortBounds(%v) = %v\n", array, sortBounds(array))

	array = []int{3, 9, 7, 6, 5}
	fmt.Printf("sortBounds(%v) = %v\n", array, sortBounds(array))
}
