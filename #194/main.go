package main

/*
Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. Imagine a set of n line segments connecting each point pi to qi. Write an algorithm to determine how many pairs of the line segments intersect.
*/

import (
	"fmt"
	"sort"
)

func inversions(numbers []int) ([]int, int) {
	if len(numbers) <= 1 {
		return numbers, 0
	}

	left, leftInversions := inversions(append([]int(nil), numbers[:len(numbers)/2]...))
	right, rightInversions := inversions(append([]int(nil), numbers[len(numbers)/2:]...))
	nbInversions := leftInversions + rightInversions

	for i, l, r := 0, 0, 0; l < len(left) || r < len(right); i++ {
		if r == len(right) || (l < len(left) && left[l] <= right[r]) {
			numbers[i] = left[l]
			l++
		} else {
			nbInversions++
			numbers[i] = right[r]
			r++
		}
	}

	return numbers, nbInversions
}

func sortMaintain(toSort []int, compare []int) []int {
	sort.Slice(toSort, func(i, j int) bool {
		return compare[i] < compare[j]
	})

	return toSort
}

func intersections(p []int, q []int) (nbIntersections int) {
	if len(p) != len(q) || len(p) == 0 {
		return -1
	}

	_, nbIntersections = inversions(sortMaintain(q, p))

	return
}

func bruteForce(p []int, q []int) (nbIntersections int) {
	if len(p) != len(q) || len(p) == 0 {
		return -1
	}

	for i := 0; i < len(p); i++ {
		for j := i + 1; j < len(p); j++ {
			if (p[i] < p[j] && q[i] > q[j]) || (p[i] > p[j] && q[i] < q[j]) {
				nbIntersections++
			}
		}
	}

	return
}

func main() {
	p := []int{1, 0, 3, 2}
	q := []int{0, 3, 1, 2}
	fmt.Println("bruteForce(p, q) =", bruteForce(p, q))
	fmt.Println("intersections(p, q) =", intersections(p, q))

	print("\n")

	p = []int{1, 0, 3, 2, -1, 4}
	q = []int{4, 1, 2, 0, 5, 3}
	fmt.Println("bruteForce(p, q) =", bruteForce(p, q))
	fmt.Println("intersections(p, q) =", intersections(p, q))
}
