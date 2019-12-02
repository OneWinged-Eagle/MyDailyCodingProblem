package main

/*
Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99
*/

import (
	"fmt"
	"strconv"
	"strings"
)

type node struct {
	val  int
	next *node
}

func (n node) String() string {
	var builder strings.Builder

	builder.WriteString(strconv.Itoa(n.val))

	if n.next != nil {
		fmt.Fprint(&builder, " -> ", n.next)
	}

	return builder.String()
}

func merge(h1 *node, h2 *node) (merged *node) {
	if h1 == nil {
		return h2
	}
	if h2 == nil {
		return h1
	}

	if h1.val <= h2.val {
		merged = h1
		merged.next = merge(h1.next, h2)
	} else {
		merged = h2
		merged.next = merge(h1, h2.next)
	}

	return
}

func cut(head *node) (left *node, right *node) {
	if head == nil {
		return
	}

	slow := head
	for fast := head; fast.next != nil && fast.next.next != nil; fast = fast.next.next {
		slow = slow.next
	}

	left, right = head, slow.next
	slow.next = nil

	return
}

func sort(head *node) *node {
	if head == nil || head.next == nil {
		return head
	}

	left, right := cut(head)

	return merge(sort(left), sort(right))
}

func main() {
	list := node{4, &node{1, &node{-3, &node{99, &node{42, nil}}}}}

	fmt.Println("list = ", list)
	fmt.Printf("sort(list) = %v\n\n", sort(&list))
}
