package main

type stack []*node

func (s *stack) push(v *node) {
	*s = append(*s, v)
}

func (s *stack) pop() *node {
	res := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return res
}
