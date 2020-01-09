package main

/*
Let X be a set of n intervals on the real line. We say that a set of points P "stabs" X if every interval in X contains at least one point in P. Compute the smallest set of points that stabs X.

For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should return [4, 9].
*/

import (
	"fmt"
	"sort"
)

type interval struct {
	start int
	end   int
}

func stabs(intervals []interval) (p []int) {
	if len(intervals) == 0 {
		return
	}

	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i].start == intervals[j].start {
			return intervals[i].end <= intervals[j].end
		}

		return intervals[i].start < intervals[j].start
	})

	end := intervals[0].end
	p = append(p, end)
	for i := 1; i < len(intervals); i++ {
		if end < intervals[i].start {
			end = intervals[i].end
			p = append(p, end)
		}
	}

	return
}

func main() {
	intervals := []interval{
		interval{1, 4},
		interval{9, 14},
		interval{4, 5},
		interval{7, 9},
		interval{1, 2},
		interval{9, 12},
		interval{1, 3},
		interval{14, 16},
	}
	fmt.Println("intervals =", intervals)
	fmt.Println("stabs(intervals) =", stabs(intervals))
}
