package main

/*
You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string. Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
*/

import "fmt"

func isBalanced(str string) bool {
	if len(str) == 0 {
		return true
	}

	minOpen, maxOpen := 0, 0
	for _, c := range str {
		switch c {
		case '(':
			minOpen++
			maxOpen++
		case ')':
			minOpen--
			maxOpen--
		case '*':
			minOpen--
			maxOpen++
		default:
			return false
		}

		if maxOpen < 0 {
			return false
		}

		if minOpen < 0 {
			minOpen = 0
		}
	}

	return minOpen == 0
}

func main() {
	fmt.Printf("isBalanced(\"(()*\") = %t\n", isBalanced("(()*"))
	fmt.Printf("isBalanced(\"(*)\") = %t\n", isBalanced("(*)"))
	fmt.Printf("isBalanced(\"(**(**)*)(*)*\") = %t\n", isBalanced("(**(**)*)(*)*"))
	fmt.Printf("isBalanced(\"()*())()*)\") = %t\n\n", isBalanced("()*())()*)"))

	fmt.Printf("isBalanced(\")*(\") = %t\n", isBalanced(")*("))
	fmt.Printf("isBalanced(\"(*()*(()\") = %t\n", isBalanced("(*()*(()"))
	fmt.Printf("isBalanced(\"(**(**)*)(*)*(\") = %t\n", isBalanced("(**(**)*)(*)*("))
}
