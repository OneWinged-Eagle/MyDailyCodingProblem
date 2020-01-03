package main

/*
Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.

For example, given the following tree:

  5
 / \
2  -5

Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.
*/

import (
	"fmt"
	"strings"
)

type node struct {
	val   int
	left  *node
	right *node
}

func (n node) String() string {
	var builder strings.Builder

	fmt.Fprintf(&builder, "node(%d", n.val)

	if n.left != nil || n.right != nil {
		fmt.Fprint(&builder, ", ", n.left)
	}

	if n.right != nil {
		fmt.Fprint(&builder, ", ", n.right)
	}

	builder.WriteRune(')')

	return builder.String()
}

func subtreeSums(root *node, sums map[int]int) int {
	if root == nil {
		return 0
	}

	sum := root.val + subtreeSums(root.left, sums) + subtreeSums(root.right, sums)
	if _, ok := sums[sum]; ok {
		sums[sum]++
	} else {
		sums[sum] = 1
	}
	return sum
}

func mostFreqSubtreeSum(root *node) (sum int) {
	sums := make(map[int]int)
	subtreeSums(root, sums)

	maxOcc := 0
	for s, occ := range sums {
		if occ > maxOcc {
			maxOcc = occ
			sum = s
		}
	}

	return
}

func main() {
	root := &node{5, &node{2, nil, nil}, &node{-5, nil, nil}}
	fmt.Println("root =", root)
	fmt.Println("mostFreqSubtreeSum(root) =", mostFreqSubtreeSum(root), "\n")

	root = &node{5, &node{2, &node{2, nil, nil}, &node{-2, nil, nil}}, &node{-5, &node{0, nil, nil}, &node{0, nil, nil}}}
	fmt.Println("root =", root)
	fmt.Println("mostFreqSubtreeSum(root) =", mostFreqSubtreeSum(root))
}
