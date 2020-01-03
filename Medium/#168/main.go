package main

/*
Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

Follow-up: What if you couldn't use any extra space?
*/

import "fmt"

func rotateMatrix(matrix [][]int) [][]int {
	size := len(matrix)

	if size <= 0 {
		return nil
	}

	for _, row := range matrix {
		if len(row) != size {
			return nil
		}
	}

	for n := 0; n < size/2; n++ {
		for i := n; i < size-1-n; i++ {
			matrix[n][i+n], matrix[i+n][size-1-n], matrix[size-1-n][size-1-i-n], matrix[size-1-i-n][n] = matrix[size-1-i-n][n], matrix[n][i+n], matrix[i+n][size-1-n], matrix[size-1-n][size-1-i-n]
		}
	}

	return matrix
}

func main() {
	matrix := [][]int{
		[]int{1, 2, 3},
		[]int{4, 5, 6},
		[]int{7, 8, 9},
	}
	fmt.Println("matrix =", matrix)
	fmt.Printf("rotateMatrix(matrix) = %v\n\n", rotateMatrix(matrix))

	matrix = [][]int{
		[]int{1, 2, 3, 4},
		[]int{5, 6, 7, 8},
		[]int{9, 10, 11, 12},
		[]int{13, 14, 15, 16},
	}
	fmt.Println("matrix =", matrix)
	fmt.Printf("rotateMatrix(matrix) = %v\n\n", rotateMatrix(matrix))

	matrix = [][]int{
		[]int{1, 2, 3, 4, 5},
		[]int{6, 7, 8, 9, 10},
		[]int{11, 12, 13, 14, 15},
		[]int{16, 17, 18, 19, 20},
		[]int{21, 22, 23, 24, 25},
	}
	fmt.Println("matrix =", matrix)
	fmt.Printf("rotateMatrix(matrix) = %v", rotateMatrix(matrix))
}
