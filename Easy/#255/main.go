package main

/*
The transitive closure of a graph is a measure of which vertices are reachable from other vertices. It can be represented as a matrix M, where M[i][j] == 1 if there is a path between vertices i and j, and otherwise 0.

For example, suppose we are given the following graph in adjacency list form:

graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]

The transitive closure of this graph would be:

[1, 1, 1, 1]
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]

Given a graph, find its transitive closure.
*/

import "fmt"

func transitive(g *graph) (matrix [][]bool) {
	matrix = make([][]bool, len(g.vertices))

	for v := range g.vertices {
		matrix[v] = make([]bool, len(g.vertices))

		for w := range g.vertices {
			matrix[v][w] = g.isPath(v, w, newSet(nil))
		}
	}

	return
}

func main() {
	g := newGraph()
	g.connect(0, 1)
	g.connect(0, 3)
	g.connect(1, 2)
	g.connect(3, 4)
	g.connect(5, 0)

	fmt.Println("graph =", g)
	fmt.Println("transitive(graph) =", transitive(g))
}
