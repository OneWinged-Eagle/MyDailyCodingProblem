package main

/*
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
*/

import "fmt"

func canMap(s1, s2 string) bool {
	runes1 := []rune(s1)
	runes2 := []rune(s2)

	if len(runes1) != len(runes2) {
		return false
	}

	runeMap := make(map[rune]rune)

	for i := 0; i < len(runes1); i++ {
		if r, ok := runeMap[runes1[i]]; ok {
			if r != runes2[i] {
				return false
			}
		} else {
			runeMap[runes1[i]] = runes2[i]
		}
	}

	return true
}

func main() {
	fmt.Printf("canMap(abc, bcd) = %v\n", canMap("abc", "bcd"))
	fmt.Printf("canMap(foo, bar) = %v", canMap("foo", "bar"))
}
