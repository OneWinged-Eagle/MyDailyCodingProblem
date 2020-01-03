package main

/*
Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.
*/

import "fmt"

type stack []int

func (s *stack) push(v int) {
	*s = append(*s, v)
}

func (s *stack) pop() int {
	res := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return res
}

type queue []int

func (q *queue) enqueue(v int) {
	*q = append(*q, v)
}

func (q *queue) dequeue() int {
	res := (*q)[0]
	*q = (*q)[1:]
	return res
}

func interleave(s *stack) *stack {
	q := &queue{}

	for i := 0; i < len(*s); i++ {
		for len(*s) > i+1 {
			q.enqueue(s.pop())
		}

		for len(*q) > 0 {
			s.push(q.dequeue())
		}
	}

	return s
}

func main() {
	s := &stack{1, 2, 3, 4, 5}

	fmt.Println("s =", s)
	fmt.Printf("interleave(s) = %v\n", interleave(s))

	s = &stack{1, 2, 3, 4}

	fmt.Println("s =", s)
	fmt.Printf("interleave(s) = %v\n", interleave(s))
}
