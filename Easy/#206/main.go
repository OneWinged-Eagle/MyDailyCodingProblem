package main

/*
A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array. For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].
*/

import "fmt"

const DONE = -1

func permutate(array []rune, permutations []int) []rune {
	if len(array) <= 0 || len(permutations) <= 0 || len(array) != len(permutations) {
		return array
	}

	for i, p := range permutations {
		index := i
		for p != DONE {
			if index != p {
				array[i], array[p] = array[p], array[i]
			}
			permutations[index] = DONE
			index = p
			p = permutations[index]
		}
	}

	return array
}

func main() {
	array := []rune{'c', 'b', 'a'}
	fmt.Println("array =", array)
	fmt.Println("permutate(array, [2, 1, 0]) =", permutate(array, []int{2, 1, 0}))

	array = []rune{'e', 'c', 'a', 'b', 'd'}
	fmt.Println("array =", array)
	fmt.Println("permutate(array, [4, 2, 0, 1, 3]) =", permutate(array, []int{4, 2, 0, 1, 3}))
}
