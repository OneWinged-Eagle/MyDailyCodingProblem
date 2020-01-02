package main

/*
Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.
*/

import "fmt"

func isPalindrome(n int) bool {
	var digits []int

	for n > 0 {
		digits = append(digits, n%10)
		n /= 10
	}

	for i := 0; i < len(digits)/2; i++ {
		if digits[i] != digits[len(digits)-i-1] {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println("isPalindrome(121) =", isPalindrome(121))
	fmt.Println("isPalindrome(888) =", isPalindrome(888))
	fmt.Println("isPalindrome(4224) =", isPalindrome(4224))

	fmt.Println("isPalindrome(678) =", isPalindrome(678))
	fmt.Println("isPalindrome(4224) =", isPalindrome(4242))
}
