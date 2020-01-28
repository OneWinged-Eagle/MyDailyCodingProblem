package main

import (
	"fmt"
	"strconv"
	"strings"
)

type node struct {
	val  int
	next *node
}

func newNode(val int) *node {
	return &node{val, nil}
}

func (n node) String() string {
	var builder strings.Builder

	builder.WriteString(strconv.Itoa(n.val))

	curr := n.next
	for curr != nil {
		fmt.Fprintf(&builder, " -> %d", curr.val)
		curr = curr.next
	}

	return builder.String()
}

type linkedList struct {
	head *node
}

func newLinkedList(numbers []int) (ll *linkedList) {
	var curr *node

	for _, nb := range numbers {
		if curr == nil {
			ll = &linkedList{newNode(nb)}
			curr = ll.head
		} else {
			curr.next = newNode(nb)
			curr = curr.next
		}
	}

	return
}

func (ll linkedList) String() string {
	return fmt.Sprintf("linkedList[%v]", ll.head)
}
