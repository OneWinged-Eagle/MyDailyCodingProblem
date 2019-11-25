package main

/*
You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.
*/

import "fmt"

func findDuplicate(elements []interface{}) (int, interface{}) {
	if len(elements) == 0 {
		return -1, nil
	}

	set := make(map[interface{}]struct{})

	for i, elem := range elements {
		if _, exists := set[elem]; exists {
			return i, elem
		}

		set[elem] = struct{}{}
	}

	return -1, nil
}

func main() {
	i, dup := findDuplicate([]interface{} {1, 2, 3, 4, 1})
	fmt.Printf("findDuplicate([1, 2, 3, 4, 1]) = (%d, %d)", i, dup)
}
