package main

/*
Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".
*/

import (
	"fmt"
	"strings"
)

func numberToCol(n int) string {
	var sb strings.Builder

	for n >= 0 {
		tmp := sb.String()
		sb.Reset()
		sb.WriteRune(65 + rune(n%26))
		sb.WriteString(tmp)
		n = n/26 - 1
	}

	return sb.String()
}

func main() {
	for n := 0; n < 1000; n++ {
		fmt.Printf("numberToCol(%d) = %s\n", n, numberToCol(n))
	}
}
