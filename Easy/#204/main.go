package main

/*
Given a complete binary tree, count the number of nodes in faster than O(n) time. Recall that a complete binary tree has every level filled except the last, and the nodes in the last level are filled starting from the left.
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

	fmt.Fprint(&builder, "node(", n.val)

	if n.left != nil || n.right != nil {
		fmt.Fprint(&builder, ", ", n.left)
	}

	if n.right != nil {
		fmt.Fprint(&builder, ", ", n.right)
	}

	builder.WriteRune(')')

	return builder.String()
}

func nbNodes(root *node) (nb int) {
	if root == nil {
		return
	}

	heightLeft, heightRight := 1, 1
	for curr := root; curr.left != nil; curr = curr.left {
		heightLeft++
	}
	for curr := root; curr.right != nil; curr = curr.right {
		heightRight++
	}

	if heightLeft == heightRight {
		return 1<<uint(heightLeft) - 1
	}

	return nbNodes(root.left) + nbNodes(root.right) + 1
}

func main() {
	root := &node{0, nil, nil}
	fmt.Printf("nbNodes(%v) = %d\n", root, nbNodes(root))

	root.left = &node{0, nil, nil}
	fmt.Printf("nbNodes(%v) = %d\n", root, nbNodes(root))

	root = &node{0, &node{0, nil, nil}, &node{0, nil, nil}}
	fmt.Printf("nbNodes(%v) = %d\n", root, nbNodes(root))

	root.left.left = &node{0, nil, nil}
	fmt.Printf("nbNodes(%v) = %d\n", root, nbNodes(root))

	root = &node{0, &node{0, &node{0, nil, nil}, &node{0, nil, nil}}, &node{0, &node{0, nil, nil}, &node{0, nil, nil}}}
	fmt.Printf("nbNodes(%v) = %d\n", root, nbNodes(root))

	root.left.left.left = &node{0, nil, nil}
	fmt.Printf("nbNodes(%v) = %d\n", root, nbNodes(root))
}
