package main

/*
Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

    5
   / \
  3   7
 / \   \
2   4   8
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

func headFromPostorder(postorder []int) (head *node) {
	if len(postorder) == 0 {
		return
	}

	head = &node{postorder[len(postorder)-1], nil, nil}

	i := len(postorder) - 2

	if i < 0 {
		return
	}

	for i >= 0 && postorder[i] > head.val {
		i--
	}

	head.left = headFromPostorder(postorder[:i+1])
	head.right = headFromPostorder(postorder[i+1 : len(postorder)-1])

	return
}

func main() {
	fmt.Printf("headFromPostorder([2, 4, 3, 8, 7, 5]) = %v", headFromPostorder([]int{2, 4, 3, 8, 7, 5}))
}
