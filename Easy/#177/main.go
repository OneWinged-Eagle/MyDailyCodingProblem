package main

/*
Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.
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

type linkedList struct {
	head   *node
	length int
}

func (l linkedList) String() string {
	return fmt.Sprintf("linkedList(%v, length = %d)", l.head, l.length)
}

func newLinkedList(data []int) (list *linkedList) {
	list = new(linkedList)
	list.length = len(data)

	if list.length == 0 {
		return
	}

	var curr *node
	for i := list.length - 1; i >= 0; i-- {
		curr = &node{data[i], curr}
	}
	list.head = curr

	return
}

func rotate(list *linkedList, k int) *linkedList {
	if k = list.length - k%list.length; k == 0 {
		return list
	}

	curr := list.head
	for i := 0; i < k-1; i++ {
		curr = curr.next
	}

	curr.next, curr = nil, curr.next

	newHead := curr
	for curr.next != nil {
		curr = curr.next
	}

	curr.next, list.head = list.head, newHead

	return list
}

func main() {
	list := newLinkedList([]int{7, 7, 3, 5})

	fmt.Println("list =", list)
	fmt.Printf("rotate(list, 2) = %v\n", rotate(list, 2))

	list = newLinkedList([]int{1, 2, 3, 4, 5})

	fmt.Println("list =", list)
	fmt.Printf("rotate(list, 3) = %v", rotate(list, 3))
}
