package main

/*
Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same. If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
*/

import (
	"fmt"
	"strings"
)

func rearrange(str string) string {
	c := newCounter(str)

	for _, freq := range c {
		if freq > len(str)/2 {
			return ""
		}
	}

	var (
		builder strings.Builder
		last    rune
	)
	for len(c) > 0 {
		for char := range c {
			if char != last {
				last = char
				builder.WriteRune(char)
				c.sub(char)
				break
			}
		}
	}

	return builder.String()
}

func main() {
	fmt.Println("rearrange('aaabbc') =", rearrange("aaabbc"))
	fmt.Println("rearrange('aaab') =", rearrange("aaab"))
}
