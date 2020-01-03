package main

import (
	"fmt"
	"strings"
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
	n           int
	stacks      []interface{}
	nextIndexes []int
	topIndexes  []int
	freeIndex   int
}

func newNStacks(n int) *nStacks {
	if n <= 0 {
		return nil
	}

	topIndexes := make([]int, n)
	for i := range topIndexes {
		topIndexes[i] = -1
	}

	return &nStacks{n, make([]interface{}, 0), make([]int, 0), topIndexes, -1}
}

func (ns *nStacks) pop(n int) interface{} {
	if n <= 0 || n > ns.n || ns.topIndexes[n-1] == -1 {
		return nil
	}

	top := ns.topIndexes[n-1]
	val := ns.stacks[top]

	ns.topIndexes[n-1] = ns.nextIndexes[top]

	ns.nextIndexes[top] = ns.freeIndex

	ns.freeIndex = top

	return val
}

func (ns *nStacks) push(val interface{}, n int) {
	if n <= 0 || n > ns.n {
		return
	}

	newTop := len(ns.stacks)

	if i := ns.freeIndex; i != -1 {
		newTop = i

		ns.stacks[ns.freeIndex] = val

		ns.freeIndex = ns.nextIndexes[i]

		ns.nextIndexes[i] = ns.topIndexes[n-1]
	} else {
		ns.stacks = append(ns.stacks, val)

		ns.nextIndexes = append(ns.nextIndexes, ns.topIndexes[n-1])
	}

	ns.topIndexes[n-1] = newTop
}

func (ns nStacks) String() string {
	var builder strings.Builder

	fmt.Fprintf(&builder, "nStacks(n = %d\n\tstacks = %v\n\tnextIndexes = %v\n\ttopIndexes = %v\n\tfreeIndex = %d)", ns.n, ns.stacks, ns.nextIndexes, ns.topIndexes, ns.freeIndex)

	return builder.String()
}

func main() {
	nstacks := newNStacks(4)

	fmt.Println("nstacks =", nstacks)

	for i := 1; i <= 4; i++ {
		nstacks.push(3*i, i)
		nstacks.push(3*i-1, i)
		nstacks.push(3*i-2, i)
	}

	fmt.Println("nstacks =", nstacks)

	for i := 1; i <= 4; i++ {
		fmt.Printf("Stack nb %d = %v, %v, %v\n", i, nstacks.pop(i), nstacks.pop(i), nstacks.pop(i))
	}

	fmt.Println("nstacks =", nstacks)

	for i := 13; i > 0; i-- {
		nstacks.push(i, 1)
	}

	fmt.Println("nstacks =", nstacks)

	for i := 13; i > 0; i-- {
		fmt.Println("nstacks.pop(1) =", nstacks.pop(1))
	}

	fmt.Println("nstacks =", nstacks)
}
