package main

/*
You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1

We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
*/

import (
	"fmt"
	"math"
)

type row []int
type triangle []row

func max(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

func helper(t triangle, nbRow, i int) int {
	if nbRow >= len(t) || i+1 >= len(t[nbRow]) {
		return 0
	}

	return max(t[nbRow][i]+helper(t, nbRow+1, i), t[nbRow][i+1]+helper(t, nbRow+1, i+1))
}

func maxPath(t triangle) (m int) {
	if len(t) == 0 || len(t[0]) != 1 {
		return 0
	}

	if len(t) == 1 {
		return t[0][0]
	}

	m = math.MinInt64
	for nbRow := 1; nbRow < len(t); nbRow++ {
		for i := 0; i < len(t[nbRow]); i++ {
			left, right := math.MinInt64, math.MinInt64

			if i > 0 {
				left = t[nbRow-1][i-1]
			}

			if i < len(t[nbRow-1]) {
				right = t[nbRow-1][i]
			}

			t[nbRow][i] += max(left, right)

			if nbRow+1 == len(t) {
				m = max(m, t[nbRow][i])
			}
		}
	}

	return
}

func main() {
	t := triangle{
		row{1},
		row{2, 3},
		row{1, 5, 1},
	}

	fmt.Printf("maxPath(%v) = %d\n", t, maxPath(t))

	t = triangle{
		row{1},
		row{2, 3},
		row{1, 5, 1},
		row{20, 10, 10, 20},
	}

	fmt.Printf("maxPath(%v) = %d\n", t, maxPath(t))

	t = triangle{
		row{1},
		row{2, 3},
		row{1, 5, 1},
		row{20, 10, 10, 20},
		row{4, 3, 10, 2, 3},
	}

	fmt.Printf("maxPath(%v) = %d\n", t, maxPath(t))
}
