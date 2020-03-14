package main

/*
MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written. They would like to give the smallest positive amount to each worker consistent with the constraint that if a developer has written more lines of code than their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.

For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].
*/

import "fmt"

func paid(line []int) []int {
	p := make([]int, len(line))

	for i := range p {
		p[i] = 1
	}

	changed := false
	for true {
		changed = false

		for i := 0; i < len(line); i++ {
			tmp := p[i]

			if i > 0 && line[i] > line[i-1] && p[i] <= p[i-1] {
				p[i] = p[i-1] + 1
			}

			if i < len(line)-1 && line[i] > line[i+1] && p[i] <= p[i+1] {
				p[i] = p[i+1] + 1
			}

			changed = changed || tmp != p[i]
		}

		if !changed {
			break
		}
	}

	return p
}

func main() {
	line := []int{10, 40, 200, 1000, 60, 30}
	fmt.Println("line =", line)
	fmt.Println("paid(line) =", paid(line))

	line = []int{1000, 400, 200, 10, 600, 300}
	fmt.Println("line =", line)
	fmt.Println("paid(line) =", paid(line))

	line = []int{1000, 400, 200, 10, 300, 600}
	fmt.Println("line =", line)
	fmt.Println("paid(line) =", paid(line))
}
