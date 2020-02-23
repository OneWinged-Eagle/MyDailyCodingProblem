package main

import (
	"strings"
)

type void struct{}
type set map[string]void

func newSet(numbers []string) (s set) {
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
	for str := range s {
		if !first {
			builder.WriteRune(' ')
		}
		builder.WriteString(str)
		first = false
	}

	builder.WriteRune(']')

	return builder.String()
}

func (s set) has(str string) bool {
	_, ok := s[str]
	return ok
}

func (s *set) add(str string) {
	if !s.has(str) {
		(*s)[str] = void{}
	}
}

func (s *set) del(str string) {
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

func (s set) any() string {
	for k := range s {
		return k
	}

	return ""
}
