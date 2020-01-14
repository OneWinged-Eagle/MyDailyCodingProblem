package main

/*
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
*/

import "fmt"

func consecutiveSetBits(n int) (count int) {
	for n != 0 {
		n = (n & (n << 1))
		count++
	}

	return
}

func main() {
	fmt.Println("consecutiveSetBits(1) =", consecutiveSetBits(1))
	fmt.Println("consecutiveSetBits(2) =", consecutiveSetBits(2))
	fmt.Println("consecutiveSetBits(4) =", consecutiveSetBits(4))
	fmt.Println("consecutiveSetBits(8) =", consecutiveSetBits(8))
	fmt.Println("consecutiveSetBits(16) =", consecutiveSetBits(16))
	fmt.Println("consecutiveSetBits(32) =", consecutiveSetBits(32))
	fmt.Println("consecutiveSetBits(64) =", consecutiveSetBits(64))
	fmt.Println("consecutiveSetBits(128) =", consecutiveSetBits(128))

	fmt.Println("consecutiveSetBits(156) =", consecutiveSetBits(156))

	fmt.Println("consecutiveSetBits(255) =", consecutiveSetBits(255))
}
