"""
Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.
"""

import numpy as np
from typing import List


def canColourise(vertice: int, colour: int, row: np.ndarray,
                 colours: List[int]) -> bool:
	for i, adjacent in enumerate(row):
		if adjacent and vertice > i and colours[i] == colour:
			return False

	return True


def colouriseVertices(graph: np.ndarray, k: int,
                      colours: List[int] = []) -> List[int]:
	if len(colours) == graph.shape[0]:
		return colours

	for i in range(k):
		if canColourise(len(colours), i, graph[len(colours)], colours):
			tmp = colouriseVertices(graph, k, colours + [i])
			if tmp:
				return tmp

	return None


graph1 = np.array([[False, True, True, False, False],
                   [True, False, True, True, False],
                   [True, True, False, True, False],
                   [False, True, True, False, True],
                   [False, False, False, True, False]])
print(f"colouriseVertices({graph1}, 3) = {colouriseVertices(graph1, 3)}")
