package main

import (
	"fmt"
	"strings"
)

type Node struct {
	val      int
	children []*Node
}

func (n Node) String() string {
	var builder strings.Builder

	fmt.Fprintf(&builder, "Node(%d", n.val)

	var first = true
	for _, child := range n.children {
		if !first {
			fmt.Fprintf(&builder, ", %v", child)
		} else {
			fmt.Fprintf(&builder, ", [%v", child)
			first = false
		}
	}

	if !first {
		builder.WriteRune(']')
	}

	builder.WriteRune(')')
	return builder.String()
}

func (n Node) reverse() (r *Node) {
	start, end := 0, len(n.children)-1

	for start < end {
		sNode, eNode := n.children[start], n.children[end]



		start++
		end--
	}

	return r
}
