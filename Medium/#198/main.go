package main

/*
Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].
*/

import (
	"fmt"
	"sort"
)

func biggest(sets [][]int) []int {
	if len(sets) == 0 {
		return nil
	}

	max, maxIndex := len(sets[0]), 0
	for i := 1; i < len(sets); i++ {
		if len(sets[i]) > max {
			max, maxIndex = len(sets[i]), i
		}
	}

	return sets[maxIndex]
}

func moduloSet(numbers []int) []int {
	length := len(numbers)
	if length <= 0 {
		return nil
	}

	sort.Slice(numbers, func(i, j int) bool {
		return numbers[i] <= numbers[j]
	})

	sets := make([][]int, length)
	for i := 0; i < length; i++ {
		sets[i] = []int{numbers[i]}
	}

	for i := 0; i < length; i++ {
		for j := 0; j < length; j++ {
			if i == j {
				continue
			}

			if numbers[j]%sets[i][len(sets[i])-1] == 0 || sets[i][len(sets[i])-1]%numbers[j] == 0 {
				sets[i] = append(sets[i], numbers[j])
			}
		}
	}

	return biggest(sets)
}

func main() {
	fmt.Println("moduloSet([3, 5, 10, 20, 21]) =", moduloSet([]int{3, 5, 10, 20, 21}))
	fmt.Println("moduloSet([1, 3, 6, 24]) =", moduloSet([]int{1, 3, 6, 24}))
}
