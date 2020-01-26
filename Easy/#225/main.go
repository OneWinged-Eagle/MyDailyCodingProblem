package main

/*
There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with the kth person, and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.
*/

import "fmt"

func makeArray(min, max int) []int {
	arr := make([]int, max-min)

	for i := min; i < max; i++ {
		arr[i-min] = i
	}

	return arr
}

func last(N, k int) int {
	if N < k || k <= 0 {
		return -1
	}
	if k == 1 {
		return N
	}

	prisoners, next := makeArray(1, N+1), k-1
	for len(prisoners) > 1 {
		prisoners = append(prisoners[:next], prisoners[next+1:]...)

		next = (next + k - 1) % len(prisoners)
	}

	return prisoners[0]
}

func main() {
	for N := 0; N <= 10; N++ {
		fmt.Printf("last(%d, 2) = %d\n", N, last(N, 2))
	}

	for k := 0; k <= 10; k++ {
		fmt.Printf("last(9, %d) = %d\n", k, last(9, k))
	}
}
