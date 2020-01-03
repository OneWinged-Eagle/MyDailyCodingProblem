package main

/*
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
*/

import "fmt"

var cache []int

func init() {
	cache = []int{0, 19}
}

func sumDigits(n int) (sum int) {
	for n > 0 {
		sum += n % 10
		n /= 10
	}

	return sum
}

func perfectNumber(n int) int {
	if n < 0 {
		return 0
	}

	for i := len(cache) - 1; i < n; i++ {
		nb := cache[i] + 9
		for sumDigits(nb) != 10 {
			nb += 9
		}

		cache = append(cache, nb)
	}

	return cache[n]
}

func main() {
	for i := 0; i < 75; i++ {
		fmt.Printf("perfectNumber(%d) = %d\n", i, perfectNumber(i))
	}
}
