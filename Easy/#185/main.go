package main

/*
Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}

and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}

return 6.
*/

import "fmt"

type pos struct {
	x int
	y int
}

type rectangle struct {
	topLeft    pos
	dimensions pos
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

func min(a, b int) int {
	if a > b {
		return b
	}

	return a
}

func intersectionArea(rect1 rectangle, rect2 rectangle) (area int) {
	bottomRight1 := pos{rect1.topLeft.x + rect1.dimensions.x, rect1.topLeft.y + rect1.dimensions.y}
	bottomRight2 := pos{rect2.topLeft.x + rect2.dimensions.x, rect2.topLeft.y + rect2.dimensions.y}

	return (min(bottomRight1.x, bottomRight2.x) - max(rect1.topLeft.x, rect2.topLeft.x)) * (min(bottomRight1.y, bottomRight2.y) - max(rect1.topLeft.y, rect2.topLeft.y))
}

func main() {
	rect1 := rectangle{pos{1, 4}, pos{3, 3}}
	rect2 := rectangle{pos{0, 5}, pos{4, 3}}

	fmt.Println("rect1 =", rect1)
	fmt.Println("rect2 =", rect2)
	fmt.Printf("intersectionArea(rect1, rect2) = %v\n", intersectionArea(rect1, rect2))

	rect1 = rectangle{pos{1, 4}, pos{0, 0}}
	rect2 = rectangle{pos{0, 5}, pos{4, 3}}

	fmt.Println("rect1 =", rect1)
	fmt.Println("rect2 =", rect2)
	fmt.Printf("intersectionArea(rect1, rect2) = %v\n", intersectionArea(rect1, rect2))
}
