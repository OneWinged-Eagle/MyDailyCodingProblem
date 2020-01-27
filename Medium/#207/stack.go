package main

type stack []int

func (s *stack) push(v int) {
	*s = append(*s, v)
}

func (s *stack) pop() int {
	res := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return res
}
