package main

/*
Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
*/

import "fmt"

func reverse(numbers []int, i, j int) []int {
	for ; i < j; i, j = i+1, j-1 {
		numbers[i], numbers[j] = numbers[j], numbers[i]
	}

	return numbers
}

func sortByReverse(numbers []int) []int {
	if len(numbers) == 0 {
		return numbers
	}

	for i := 0; i < len(numbers); {
		min := numbers[i]
		indexes := []int{i}

		for j := i + 1; j < len(numbers); j++ {
			if numbers[j] == min {
				indexes = append(indexes, j)
			} else if numbers[j] < min {
				min = numbers[j]
				indexes = []int{j}
			}
		}

		for _, index := range indexes {
			reverse(numbers, i, index)
			i++
		}
	}

	return numbers
}

func main() {
	fmt.Println("sortByReverse([4, 5, 1, 3, 2, 0]) =", sortByReverse([]int{4, 5, 1, 3, 2, 0}))
	fmt.Println("sortByReverse([1, 1, 1, 1, 1, 0]) =", sortByReverse([]int{1, 1, 1, 1, 1, 0}))
	fmt.Println("sortByReverse([0, 1, 2, 0, 2, 1, 1, 2, 0]) =", sortByReverse([]int{0, 1, 2, 0, 2, 1, 1, 2, 0}))
}
