package main

/*
What will this code print out?

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()

How can we make it print out what we apparently want?
*/

import "fmt"

func makeFunctions() (functions []func()) {
	for i := 1; i <= 3; i++ {
		a := i
		functions = append(functions, func() {
			fmt.Println(a)
		})
	}

	return
}

func main() {
	functions := makeFunctions()

	for _, f := range functions {
		f()
	}
}
