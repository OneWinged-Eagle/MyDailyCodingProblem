package main

/*
Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances. And in every even call of getInstance(), return the first instance and in every odd call of getInstance(), return the second instance.
*/

import (
	"fmt"
	"sync"
)

type singleton struct {
	firstInstance  int
	secondInstance int
}

var (
	once sync.Once
	s    *singleton
	b    bool
)

func getInstance() *int {
	if !b {
		b = true
		return &s.firstInstance
	}

	b = false
	return &s.secondInstance
}

func newInstance(first, second int) func() *int {
	once.Do(func() {
		s = &singleton{first, second}
	})

	return getInstance
}

func main() {
	getinstance := newInstance(1, 2)

	fmt.Printf("getinstance() = %d (should be 1)\n", *getinstance())
	fmt.Printf("getinstance() = %d (should be 2)\n", *getinstance())

	*getinstance() = 42
	*getinstance() = 77

	fmt.Printf("getinstance() = %d (should be 42)\n", *getinstance())
	fmt.Printf("getinstance() = %d (should be 77)\n", *getinstance())
}
