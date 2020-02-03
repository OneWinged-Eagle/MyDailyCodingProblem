package main

/*
Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.
*/

import "fmt"

func fib(n int) int {
	if n <= 0 {
		return 0
	}

	last, curr := 0, 1

	for n > 1 {
		last, curr = curr, curr+last
		n--
	}

	return curr
}

func main() {
	for n := 0; n <= 20; n++ {
		fmt.Printf("fib(%d) = %d\n", n, fib(n))
	}
}
