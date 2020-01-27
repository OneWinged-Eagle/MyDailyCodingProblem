package main

import (
	"fmt"
	"strings"
)

type graph struct {
	vertices    set
	adjacencies map[int]set
}

func newGraph() *graph {
	return &graph{newSet(nil), make(map[int]set)}
}

func (g graph) String() string {
	var builder strings.Builder

	fmt.Fprintf(&builder, "graph(\n\tvertices: %v\n\tadjacencies: %v\n)", g.vertices, g.adjacencies)

	return builder.String()
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
