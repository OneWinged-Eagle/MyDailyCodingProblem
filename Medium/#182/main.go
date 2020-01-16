package main

/*
A graph is minimally-connected if it is connected and there is no edge that can be removed while still leaving the graph connected. For example, any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected. You can choose to represent the graph as either an adjacency matrix or adjacency list.
*/

import "fmt"

func minimallyConnected(g *graph) bool {
	var (
		vertex  int
		q       queue
		visited set
		parents map[int]int
	)

	vertex = g.anyVertex()
	q.enqueue(vertex)
	visited = newSet([]int{vertex})
	parents = make(map[int]int, len(g.vertices)-1)

	for len(q) > 0 {
		curr := q.dequeue()

		for v := range g.adjacencies[curr] {
			if !visited.has(v) {
				q.enqueue(v)
				visited.add(v)
				parents[v] = curr
			} else if parents[curr] != v {
				return false
			}
		}
	}

	return true
}

func main() {
	g := newGraph()
	g.connect(4, 5)
	g.connect(5, 6)
	g.connect(6, 7)
	g.connect(5, 42)
	g.connect(6, 100)

	fmt.Println("g =", g)
	fmt.Println("minimallyConnected(g) =", minimallyConnected(g))

	g.connect(77, 5)

	fmt.Println("g =", g)
	fmt.Println("minimallyConnected(g) =", minimallyConnected(g))

	g.connect(100, 42)

	fmt.Println("g =", g)
	fmt.Println("minimallyConnected(g) =", minimallyConnected(g))
}
