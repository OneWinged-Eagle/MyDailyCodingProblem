package main

/*
You are given a list of data entries that represent entries and exits of groups of people into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building. Return it as a pair of (start, end) timestamps. You can assume the building always starts off and ends up empty, i.e. with 0 people inside.
*/

import (
	"fmt"
	"sort"
)

type entry struct {
	Timestamp int
	Count     int
	Type      string
}

func busiest(entries []entry) (start, end int) {
	sort.Slice(entries, func(i, j int) bool {
		return entries[i].Timestamp < entries[j].Timestamp
	})

	count, maxCount := 0, 0
	for _, e := range entries {
		switch e.Type {
		case "enter":
			count += e.Count
		case "exit":
			count -= e.Count
		default:
			return -1, -1
		}

		if count < 0 {
			return -1, -1
		}

		if count < maxCount {
			end = e.Timestamp
		} else if count > maxCount {
			maxCount = count
			start = e.Timestamp
		}
	}

	if count != 0 {
		return -1, -1
	}

	return
}

func main() {
	entries := []entry{
		entry{Timestamp: 4, Count: 6, Type: "enter"},
		entry{Timestamp: 9, Count: 11, Type: "enter"},
		entry{Timestamp: 10, Count: 12, Type: "exit"},
		entry{Timestamp: 8, Count: 4, Type: "exit"},
		entry{Timestamp: 6, Count: 2, Type: "exit"},
		entry{Timestamp: 7, Count: 3, Type: "exit"},
		entry{Timestamp: 2, Count: 2, Type: "enter"},
		entry{Timestamp: 0, Count: 3, Type: "enter"},
		entry{Timestamp: 5, Count: 1, Type: "exit"},
		entry{Timestamp: 1, Count: 4, Type: "enter"},
		entry{Timestamp: 3, Count: 4, Type: "exit"},
	}

	fmt.Println("entries =", entries)
	start, end := busiest(entries)
	fmt.Printf("busiest(entries) = (%d, %d) | Should be (9, 10)", start, end)
}
