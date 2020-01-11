package main

/*
A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

    if n is even, the next number in the sequence is n / 2
    if n is odd, the next number in the sequence is 3n + 1

It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
*/

import "fmt"

func collatz(n int) int {
	if n%2 == 0 {
		return n / 2
	}

	return 3*n + 1
}

func sequence(n int) (size int) {
	if n <= 0 {
		return n
	}

	for ; n != 1; n = collatz(n) {
		size++
	}

	return size + 1
}

func main() {
	longest := 0
	for n := 0; n <= 1000000; n++ {
		if tmp := sequence(n); tmp > longest {
			longest = tmp
			fmt.Printf("New longest sequence at n = %d with %d numbers.\n", n, longest)
		}
	}
}
