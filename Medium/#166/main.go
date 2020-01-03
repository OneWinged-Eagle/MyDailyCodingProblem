package main

import (
	"errors"
	"fmt"
)

/*
Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

    next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
    has_next(): returns whether or not the iterator still has elements left.

For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
*/

type matrixIterator struct {
	matrix [][]int
	y      int
	x      int
}

func newMatrixIterator(matrix [][]int) *matrixIterator {
	y := 0
	for y < len(matrix) && len(matrix[y]) == 0 {
		y++
	}

	return &matrixIterator{matrix, y, 0}
}

func (mi *matrixIterator) next() (int, error) {
	if !mi.has_next() {
		return -1, errors.New("matrixIterator exhausted")
	}

	nb := mi.matrix[mi.y][mi.x]

	mi.x++
	if mi.x >= len(mi.matrix[mi.y]) {
		mi.x = 0
		mi.y++
		for mi.y < len(mi.matrix) && len(mi.matrix[mi.y]) == 0 {
			mi.y++
		}
	}

	return nb, nil
}

func (mi matrixIterator) has_next() bool {
	return mi.y < len(mi.matrix) && mi.x < len(mi.matrix[mi.y])
}

func main() {
	iterator := newMatrixIterator([][]int{
		[]int{},
		[]int{1, 2},
		[]int{},
		[]int{3},
		[]int{},
		[]int{4, 5, 6},
		[]int{},
	})

	for iterator.has_next() {
		nb, err := iterator.next()
		if err != nil {
			panic(err)
		}

		fmt.Print(nb)
	}
}
