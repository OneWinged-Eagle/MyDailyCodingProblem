package main

/*
You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}

return true as the first and third rectangle overlap each other.
*/

import (
	"fmt"
	"sort"
)

type pos struct {
	x int
	y int
}

type dim struct {
	x uint
	y uint
}

type rect struct {
	topLeft    pos
	dimensions dim
}

func overlapping(rectangles []rect) bool {
	if len(rectangles) <= 1 {
		return false
	}

	sort.Slice(rectangles, func(i, j int) bool {
		return rectangles[i].topLeft.x <= rectangles[j].topLeft.x
	})

	for i := 1; i < len(rectangles); i++ {
		if rectangles[i].topLeft.x < rectangles[i-1].topLeft.x+int(rectangles[i-1].dimensions.x) {
			return true
		}
	}

	return false
}

func main() {
	rectangles := []rect{
		rect{pos{1, 4}, dim{3, 3}},
		rect{pos{-1, 3}, dim{2, 1}},
		rect{pos{0, 5}, dim{4, 3}},
	}

	fmt.Println("rectangles =", rectangles)
	fmt.Printf("overlapping(rectangles) = %v\n", overlapping(rectangles))
}
