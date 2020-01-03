package main

/*
Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]

Return 4.
*/

import "fmt"

type stack []int

func (s *stack) push(v int) {
	*s = append(*s, v)
}

func (s *stack) pop() int {
	res := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return res
}

func (s *stack) peek() int {
	return (*s)[len(*s)-1]
}

func largest(row []int) (area int) {
	if len(row) == 0 {
		return
	}

	s := make(stack, len(row))

	for i := 0; i < len(row); {
		if len(s) == 0 || row[s.peek()] <= row[i] {
			s.push(i)
			i++
		} else {
			newArea := row[s.pop()]

			if len(s) == 0 {
				newArea *= i
			} else {
				newArea *= (i - s.peek() - 1)
			}

			if newArea > area {
				area = newArea
			}
		}
	}

	for len(s) != 0 {
		newArea := row[s.pop()]

		if len(s) == 0 {
			newArea *= len(row)
		} else {
			newArea *= (len(row) - s.peek() - 1)
		}

		if newArea > area {
			area = newArea
		}
	}

	return
}

func largestRectangleArea(matrix [][]int) (area int) {
	if len(matrix) == 0 {
		return -1
	}

	for _, r := range matrix {
		if len(r) != len(matrix[0]) {
			return -1
		}

		for _, val := range r {
			if val != 0 && val != 1 {
				return -1
			}
		}
	}

	row := make([]int, len(matrix[0]))
	copy(row, matrix[0])

	area = largest(row)

	for y := 1; y < len(matrix); y++ {
		for x, val := range matrix[y] {
			row[x] = row[x]*val + val
		}

		if a := largest(row); a > area {
			area = a
		}
	}

	return
}

func main() {
	matrix := [][]int{
		[]int{1, 0, 0, 0},
		[]int{1, 0, 1, 1},
		[]int{1, 0, 1, 1},
		[]int{0, 1, 0, 0},
	}

	fmt.Println("matrix =", matrix)
	fmt.Printf("largestRectangleArea(matrix) = %v\n", largestRectangleArea(matrix))

	matrix = [][]int{
		[]int{1, 0, 0, 0},
		[]int{1, 0, 1, 1},
		[]int{1, 0, 1, 1},
		[]int{0, 1, 1, 1},
	}

	fmt.Println("matrix =", matrix)
	fmt.Printf("largestRectangleArea(matrix) = %v\n", largestRectangleArea(matrix))

	matrix = [][]int{
		[]int{1, 0, 0, 0},
		[]int{1, 0, 1, 1},
		[]int{1, 1, 1, 1},
		[]int{1, 1, 1, 1},
	}

	fmt.Println("matrix =", matrix)
	fmt.Printf("largestRectangleArea(matrix) = %v\n", largestRectangleArea(matrix))
}
