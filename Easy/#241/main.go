package main

/*
In academia, the h-index is a metric used to calculate the impact of a researcher's papers. It is calculated as follows:

A researcher has index h if at least h of her N papers have h citations each. If there are multiple h satisfying this formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]. Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.
*/

import "fmt"

func hIndex(citations []int) (h int) {
	sm := newSortedMap()

	for _, citation := range citations {
		sm.set(citation, sm.get(citation, 0)+1)
	}

	total := 0

	for i := len(sm.keys) - 1; i >= 0; i-- {
		total += sm.m[sm.keys[i]]

		if total >= sm.keys[i] {
			return sm.keys[i]
		}
	}

	return 0
}

func main() {
	citations := []int{4, 3, 0, 1, 5}
	fmt.Printf("hIndex(%v) = %d\n", citations, hIndex(citations))

	citations = []int{4, 3, 0, 1, 5, 4, 6}
	fmt.Printf("hIndex(%v) = %d\n", citations, hIndex(citations))
}
