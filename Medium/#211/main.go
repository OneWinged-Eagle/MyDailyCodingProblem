package main

/*
Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
*/

import "fmt"

func search(str, pattern string) (indices []int) {
	if len(str) == 0 || len(pattern) == 0 || len(pattern) > len(str) {
		return
	}

	for i := range str {
		n := 0
		for ; i+n < len(str) && n < len(pattern) && str[i+n] == pattern[n]; n++ {
		}
		if n == len(pattern) {
			indices = append(indices, i)
		}
	}

	return
}

func main() {
	fmt.Println("search('abracadabra', 'abr') = ", search("abracadabra", "abr"))
}
