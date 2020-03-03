package main

/*
The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.

Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.
*/

import (
	"fmt"
	"math"
)

func egyptian(a, b int) (fractions []int) {
	for a != 0 {
		tmp := int(math.Ceil(float64(b) / float64(a)))
		fractions = append(fractions, tmp)
		a, b = tmp*a-b, b*tmp
	}

	return
}

func main() {
	fmt.Println("egyptian(4, 13) =", egyptian(4, 13))
}
