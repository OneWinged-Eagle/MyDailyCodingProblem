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
}

func (g graph) isPath(v, w int, visited set) bool {
	if v == w {
		return true
	}

	visited.add(v)

	if s, ok := g.adjacencies[v]; ok {
		if s.has(w) {
			return true
		} else {
			for next := range s {
				if !visited.has(next) && g.isPath(next, w, visited) {
					return true
				}
			}
		}
	}

	return false
}
