package main

/*
Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
*/

import "fmt"

func min(numbers []int) (m int) {
	if len(numbers) == 0 {
		return
	}

	m = numbers[0]
	for i := 1; i < len(numbers); i++ {
		if numbers[i] < m {
			m = numbers[i]
		}
	}

	return
}

func greatestDenominator1(numbers []int) (denom int) {
	mini := min(numbers)

	denom = mini
	for denom > 1 {
		ok := true
		for _, nb := range numbers {
			if nb%denom != 0 {
				ok = false
				break
			}
		}

		if ok {
			return
		}

		denom--
		for mini%denom != 0 {
			denom--
		}
	}

	return
}

func gcd(a, b int) int {
	for b > 0 {
		a, b = b, a%b
	}

	return a
}

func greatestDenominator(numbers []int) (denom int) {
	if len(numbers) == 0 {
		return
	}

	denom = numbers[0]
	for i := 1; i < len(numbers); i++ {
		denom = gcd(denom, numbers[i])
	}

	return
}

func main() {
	numbers := []int{42, 56, 28}

	fmt.Printf("greatestDenominator(%v) = %v\n", numbers, greatestDenominator(numbers))
}
