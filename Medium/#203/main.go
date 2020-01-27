package main

/*
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
*/

import "fmt"

func minElem(numbers []int) int {
	if len(numbers) == 0 {
		return 0
	}

	start, end := 0, len(numbers)-1
	for start < end-1 {
		middle := (start + end) / 2

		if numbers[start] <= numbers[middle] {
			if numbers[middle] <= numbers[end] {
				return numbers[start]
			}
			start = middle
		} else {
			if numbers[middle] <= numbers[end] {
				end = middle
			} else {
				panic("impossible")
			}
		}
	}

	if numbers[end] < numbers[start] {
		return numbers[end]
	}

	return numbers[start]
}

func main() {
	fmt.Println("minElem([3, 4, 5, 7]) =", minElem([]int{3, 4, 5, 7}))
	fmt.Println("minElem([7, 3, 4, 5]) =", minElem([]int{7, 3, 4, 5}))
	fmt.Println("minElem([5, 7, 3, 4]) =", minElem([]int{5, 7, 3, 4}))
	fmt.Println("minElem([4, 5, 7, 3]) =", minElem([]int{4, 5, 7, 3}))
	fmt.Println("minElem([3, 4, 5, 7]) =", minElem([]int{3, 4, 5, 7}))

	fmt.Println()

	fmt.Println("minElem([3, 4, 5, 7, 10]) =", minElem([]int{3, 4, 5, 7, 10}))
	fmt.Println("minElem([10, 3, 4, 5, 7]) =", minElem([]int{10, 3, 4, 5, 7}))
	fmt.Println("minElem([7, 10, 3, 4, 5]) =", minElem([]int{7, 10, 3, 4, 5}))
	fmt.Println("minElem([5, 7, 10, 3, 4]) =", minElem([]int{5, 7, 10, 3, 4}))
	fmt.Println("minElem([4, 5, 7, 10, 3]) =", minElem([]int{4, 5, 7, 10, 3}))
	fmt.Println("minElem([3, 4, 5, 7, 10]) =", minElem([]int{3, 4, 5, 7, 10}))

	fmt.Println()

	fmt.Println("minElem([3, 5, 5, 7, 10]) =", minElem([]int{3, 5, 5, 7, 10}))
	fmt.Println("minElem([10, 3, 5, 5, 7]) =", minElem([]int{10, 3, 5, 5, 7}))
	fmt.Println("minElem([7, 10, 3, 5, 5]) =", minElem([]int{7, 10, 3, 5, 5}))
	fmt.Println("minElem([5, 7, 10, 3, 5]) =", minElem([]int{5, 7, 10, 3, 5}))
	fmt.Println("minElem([5, 5, 7, 10, 3]) =", minElem([]int{5, 5, 7, 10, 3}))
	fmt.Println("minElem([3, 5, 5, 7, 10]) =", minElem([]int{3, 5, 5, 7, 10}))

	fmt.Println()

	fmt.Println("minElem([3, 4, 5, 10, 10]) =", minElem([]int{3, 4, 5, 10, 10}))
	fmt.Println("minElem([10, 3, 4, 5, 10]) =", minElem([]int{10, 3, 4, 5, 10}))
	fmt.Println("minElem([10, 10, 3, 4, 5]) =", minElem([]int{10, 10, 3, 4, 5}))
	fmt.Println("minElem([5, 10, 10, 3, 4]) =", minElem([]int{5, 10, 10, 3, 4}))
	fmt.Println("minElem([4, 5, 10, 10, 3]) =", minElem([]int{4, 5, 10, 10, 3}))
	fmt.Println("minElem([3, 4, 5, 10, 10]) =", minElem([]int{3, 4, 5, 10, 10}))

	fmt.Println()

	fmt.Println("minElem([3, 3, 5, 10, 10]) =", minElem([]int{3, 3, 5, 10, 10}))
	fmt.Println("minElem([10, 3, 3, 5, 10]) =", minElem([]int{10, 3, 3, 5, 10}))
	fmt.Println("minElem([10, 10, 3, 3, 5]) =", minElem([]int{10, 10, 3, 3, 5}))
	fmt.Println("minElem([5, 10, 10, 3, 3]) =", minElem([]int{5, 10, 10, 3, 3}))
	fmt.Println("minElem([3, 5, 10, 10, 3]) =", minElem([]int{3, 5, 10, 10, 3}))
	fmt.Println("minElem([3, 3, 5, 10, 10]) =", minElem([]int{3, 3, 5, 10, 10}))
}
