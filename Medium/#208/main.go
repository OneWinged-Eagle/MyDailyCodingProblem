package main

/*
Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution could be 1 -> 0 -> 5 -> 8 -> 3.
*/

import "fmt"

func partition(ll *linkedList, k int) *linkedList {
	var lesser, currLesser, greater, currGreater *node

	curr := ll.head
	for curr != nil {
		if curr.val < k {
			if currLesser == nil {
				currLesser = curr
				lesser = currLesser
			} else {
				currLesser.next = curr
				currLesser = currLesser.next
			}
		} else {
			if currGreater == nil {
				currGreater = curr
				greater = currGreater
			} else {
				currGreater.next = curr
				currGreater = currGreater.next
			}
		}
		curr = curr.next
	}

	if lesser == nil {
		lesser = greater
	} else {
		currLesser.next = greater
	}

	if currGreater != nil {
		currGreater.next = nil
	}

	return &linkedList{lesser}
}

func main() {
	for k := -1; k <= 10; k++ {
		ll := newLinkedList([]int{5, 1, 8, 0, 3})
		fmt.Println("ll = ", ll)
		fmt.Printf("partition(ll, %d) = %v\n\n", k, partition(ll, k))
	}
}
