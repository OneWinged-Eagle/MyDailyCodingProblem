package main

/*
Given an integer, find the next permutation of it in absolute order. For example, given 48975, the next permutation would be 49578
*/

import (
	"fmt"
	"sort"
)

func digitsToInt(digits []int) (n int) {
	mult := 1
	for _, d := range digits {
		n += d * mult
		mult *= 10
	}
	return
}

func intToDigits(n int) (digits []int) {
	for n > 0 {
		digits = append(digits, n%10)
		n /= 10
	}
	return
}

func nextPerm(n int) int {
	digits := intToDigits(n)

	i := 1
	for ; i < len(digits); i++ {
		if digits[i] < digits[i-1] {
			break
		}
	}

	if i >= len(digits) {
		return -1
	}

	toSwitch := -1
	for j := 0; j <= i; j++ {
		if digits[j] > digits[i] && (toSwitch == -1 || digits[j] < digits[toSwitch]) {
			toSwitch = j
		}
	}

	if toSwitch == -1 {
		return -1
	}

	digits[i], digits[toSwitch] = digits[toSwitch], digits[i]

	sort.Slice(digits[:i], func(a, b int) bool {
		return digits[a] > digits[b]
	})

	return digitsToInt(digits)
}

func main() {
	fmt.Println("nextPerm(48975) =", nextPerm(48975))
}
