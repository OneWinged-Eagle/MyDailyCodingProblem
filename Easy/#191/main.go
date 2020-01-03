package main

/*
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.
*/

import (
	"fmt"
	"sort"
)

type interval struct {
	start int
	end   int
}

func noOverlaps(intervals []interval) (toRm int) {
	if len(intervals) <= 1 {
		return
	}

	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i].start == intervals[j].start {
			return intervals[i].end <= intervals[j].end
		}

		return intervals[i].start <= intervals[j].start
	})

	start, end := intervals[0].start, intervals[0].end
	for _, inter := range intervals[1:] {
		if inter.start == start && inter.end >= end {
			end = inter.end
			toRm++
		} else if inter.start > start {
			if inter.start < end {
				toRm++
			} else {
				start = inter.start
				end = inter.end
			}
		}
	}

	return
}

func main() {
	intervals := []interval{
		interval{0, 1},
		interval{1, 2},
	}

	fmt.Println("intervals =", intervals)
	fmt.Printf("noOverlaps(intervals) = %v\n", noOverlaps(intervals))

	intervals = []interval{
		interval{7, 9},
		interval{2, 4},
		interval{5, 8},
	}

	fmt.Println("intervals =", intervals)
	fmt.Printf("noOverlaps(intervals) = %v\n", noOverlaps(intervals))

	intervals = []interval{
		interval{7, 9},
		interval{2, 4},
		interval{5, 8},
		interval{1, 3},
	}

	fmt.Println("intervals =", intervals)
	fmt.Printf("noOverlaps(intervals) = %v\n", noOverlaps(intervals))
}
