package main

/*
You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
*/

import (
	"fmt"
	"math/rand"
	"time"
)

func init() {
	rand.Seed(time.Now().UnixNano())
}

func generateRandom(numbers []int, probabilities []float64) int {
	if len(numbers) != len(probabilities) || len(numbers) == 0 {
		return 0
	}

	for i := 1; i < len(probabilities); i++ {
		probabilities[i] += probabilities[i-1]
	}

	r := rand.Float64()

	for i := len(probabilities) - 1; i > 0; i-- {
		if r >= probabilities[i-1] {
			return numbers[i]
		}
	}

	return numbers[0]
}

func main() {
	numbers := make([]int, 5)

	for i := 0; i < 10000; i++ {
		numbers[generateRandom([]int{0, 1, 2, 3, 4}, []float64{0.04, 0.24, 0.32, 0.22, 0.18})]++
	}

	fmt.Printf("numbers = %v\n", numbers)
}
