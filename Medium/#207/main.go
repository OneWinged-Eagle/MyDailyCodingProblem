package main

/*
Given an undirected graph G, check whether it is bipartite. Recall that a graph is bipartite if its vertices can be divided into two independent sets, U and V, such that no edge connects vertices of the same set.
*/

import "fmt"

func isBipartite(g *graph) bool {
	vertices, nbParts := g.vertices.copy(), 0

	for len(vertices) > 0 {
		var s stack
		s.push(vertices.any())
		visited := newSet(nil)
		for len(s) > 0 {
			curr := s.pop()
			vertices.del(curr)
			visited.add(curr)

			for v := range g.adjacencies[curr] {
				if !visited.has(v) {
					s.push(v)
				}
			}
		}
		nbParts++

		if nbParts > 2 {
			return false
		}
	}

	return nbParts == 2
}

func main() {
	g := newGraph()
	g.connect(1, 2)
	g.connect(1, 3)
	g.connect(2, 3)
	g.connect(4, 5)
	fmt.Println(g)
	fmt.Println("isBipartite(g) =", isBipartite(g))

	fmt.Println()

	g.connect(3, 4)
	fmt.Println(g)
	fmt.Println("isBipartite(g) =", isBipartite(g))
}
