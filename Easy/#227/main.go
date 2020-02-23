package main

/*
Boggle is a game played on a 4 x 4 grid of letters. The goal is to find as many words as possible that can be formed by a sequence of adjacent letters in the grid, using each cell at most once. Given a game board and a dictionary of valid words, implement a Boggle solver.
*/

import "fmt"

type board [4][4]rune

func findWords(b board, y, x int, ret rune, curr *Node) (words []string) {
	if curr.word != "" {
		words = append(words, curr.word)
	}

	b[y][x] = 0

	if y > 0 {
		if next, ok := curr.children[b[y-1][x]]; ok {
			words = append(words, findWords(b, y-1, x, b[y-1][x], next)...)
		}
	}

	if x < 3 {
		if next, ok := curr.children[b[y][x+1]]; ok {
			words = append(words, findWords(b, y, x+1, b[y][x+1], next)...)
		}
	}

	if y < 3 {
		if next, ok := curr.children[b[y+1][x]]; ok {
			words = append(words, findWords(b, y+1, x, b[y+1][x], next)...)
		}
	}

	if x > 0 {
		if next, ok := curr.children[b[y][x-1]]; ok {
			words = append(words, findWords(b, y, x-1, b[y][x-1], next)...)
		}
	}

	b[y][x] = ret

	return
}

func boggled(b board, dictionary set) (words []string) {
	curr := newTrie(dictionary).head

	for y, row := range b {
		for x, cell := range row {
			if next, ok := curr.children[cell]; ok {
				words = append(words, findWords(b, y, x, cell, next)...)
			}
		}
	}

	return
}

func main() {
	b := [4][4]rune{
		[4]rune{'g', 'r', 'i', 'd'},
		[4]rune{'a', 'm', 'e', 'l'},
		[4]rune{'e', 't', 't', 'u'},
		[4]rune{'r', 's', 'e', 'o'},
	}
	dictionary := newSet([]string{"game", "played", "grid", "letter", "letters", "goal", "find", "many", "words", "formed", "seoul"})

	fmt.Println("board =", b)
	fmt.Println("dictionary =", dictionary)
	fmt.Println("boggled(board, dictionary) =", boggled(b, dictionary))
}
