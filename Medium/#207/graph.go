package main

import (
	"fmt"
)

type graph struct {
	vertices    set
	adjacencies map[int]set
}

func newGraph() *graph {
	return &graph{newSet(nil), make(map[int]set)}
}

func (g graph) String() string {
	return fmt.Sprintf("graph(\n\tvertices: %v\n\tadjacencies: %v\n)", g.vertices, g.adjacencies)
}

func (g *graph) connect(v, w int) {
	g.vertices.add(v)
	g.vertices.add(w)

	if s, ok := g.adjacencies[v]; ok {
		s.add(w)
	} else {
		g.adjacencies[v] = newSet([]int{w})
	}

	if s, ok := g.adjacencies[w]; ok {
		s.add(v)
	} else {
		g.adjacencies[w] = newSet([]int{v})
	}
}

func (g graph) anyVertex() int {
	for k := range g.vertices {
		return k
	}

	return 0
}
