package main

import (
	"fmt"
)

/*
Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass
*/

type nStacks struct {
	n     int
	stack []interface{}
	lens  []int
}

func newNStacks(n int) *nStacks {
	if n <= 0 {
		return nil
	}

	return &nStacks{n, make([]interface{}, 0), make([]int, n)}
}

func (ns *nStacks) pop(n int) interface{} {
	if n <= 0 || n > ns.n || ns.lens[n-1] == 0 {
		return nil
	}

	ns.lens[n-1]--

	i := ns.lens[n-1]*ns.n + n - 1
	val := ns.stack[i]

	for _, l := range ns.lens {
		if l > ns.lens[n-1] {
			return val
		}
	}

	ns.stack = ns.stack[:len(ns.stack)-ns.n]

	return val
}

func (ns *nStacks) push(val interface{}, n int) {
	if n <= 0 || n > ns.n {
		return
	}

	i := ns.lens[n-1]*ns.n + n - 1
	if i >= len(ns.stack) {
		toAppend := make([]interface{}, ns.n)
		toAppend[n-1] = val
		ns.stack = append(ns.stack, toAppend...)
	} else {
		ns.stack[i] = val
	}

	ns.lens[n-1]++
}

func main() {
	nstacks := newNStacks(4)

	for i := 1; i <= 4; i++ {
		nstacks.push(3*i, i)
		nstacks.push(3*i-1, i)
		nstacks.push(3*i-2, i)
	}

	for i := 1; i <= 4; i++ {
		fmt.Println("nstacks.stack =", nstacks.stack)
		fmt.Printf("Stack nb %d = %v, %v, %v\n", i, nstacks.pop(i), nstacks.pop(i), nstacks.pop(i))
		fmt.Println("nstacks.stack =", nstacks.stack)
	}

	for i := 10; i > 0; i-- {
		nstacks.push(i, 1)
	}

	for i := 10; i > 0; i-- {
		fmt.Println("nstacks.stack =", nstacks.stack)
		fmt.Println("nstacks.pop(1) =", nstacks.pop(1))
	}

	fmt.Println("nstacks.stack =", nstacks.stack)
}
