package main

type node struct {
	left  *node
	right *node
}

func newNode(left *node, right *node) *node {
	return &node{left, right}
}
