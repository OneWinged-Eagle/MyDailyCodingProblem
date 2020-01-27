package main

import (
	"strconv"
	"strings"
)

type void struct{}
type set map[int]void

func newSet(numbers []int) (s set) {
	s = make(set, len(numbers))
	for _, str := range numbers {
		s.add(str)
	}

	return
}

func (s set) String() string {
	var builder strings.Builder

	builder.WriteString("set[")

	first := true
	for nb := range s {
		if !first {
			builder.WriteRune(' ')
		}
		builder.WriteString(strconv.Itoa(nb))
		first = false
	}

	builder.WriteRune(']')

	return builder.String()
}

func (s set) has(str int) bool {
	_, ok := s[str]
	return ok
}

func (s *set) add(str int) {
	if !s.has(str) {
		(*s)[str] = void{}
	}
}

func (s *set) del(str int) {
	if s.has(str) {
		delete(*s, str)
	}
}

func (s set) copy() (c set) {
	c = newSet(nil)
	for k := range s {
		c.add(k)
	}

	return
}

func (s set) any() int {
	for k := range s {
		return k
	}

	return 0
}
