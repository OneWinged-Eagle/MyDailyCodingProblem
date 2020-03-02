package main

type node struct {
	val   int
	left  *node
	right *node
}

func newNode(val int, left, right *node) *node {
	return &node{val, left, right}
}
