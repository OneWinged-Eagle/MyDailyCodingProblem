package main

/*
Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number.
*/

import "fmt"

var lastPow int
var sevenish []int

func getNSevenish(n int) int {
	if n <= 0 {
		return -1
	}

	for len(sevenish) < n {
		pow := 1
		if lastPow != 0 {
			pow = lastPow * 7
		}
		lastPow = pow

		sevenish = append(sevenish, pow)

		for _, s := range sevenish {
			if s == pow {
				break
			}

			sevenish = append(sevenish, pow+s)
		}
	}

	return sevenish[n-1]
}

func main() {
	for i := 0; i <= 10; i++ {
		fmt.Printf("getNSevenish(%d) = %d\n", i, getNSevenish(i))
	}
}
