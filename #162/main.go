package main

/*
Given a list of words, return the shortest unique prefix of each word. For example, given the list:

    dog
    cat
    apple
    apricot
    fish

Return the list:

    d
    c
    app
    apr
		f
*/

import "fmt"

type Node struct {
	count int
	children map[rune]*Node
}

func newNode(char rune) (node *Node) {
	return &Node{count: 1, children: make(map[rune]*Node)}
}

type Trie struct {
	head *Node
}

func newTrie(words []string) (trie *Trie) {
	trie = &Trie{head: newNode(0)}

	for _, word := range words {
		curr := trie.head

		for _, char := range word {
			if _, exists := curr.children[char]; exists {
				curr.children[char].count += 1
			} else {
				curr.children[char] = newNode(char)
			}

			curr = curr.children[char]
		}
	}

	return
}

func getShortestPrefixes(words []string) (prefixes []string) {
	trie := newTrie(words)

	for _, word := range words {
		curr := trie.head

		for i, char := range word {
			if curr.children[char].count == 1 {
				prefixes = append(prefixes, word[:i + 1])
				break
			}

			curr = curr.children[char]
		}

		if len(curr.children) == 0 {
			prefixes = append(prefixes, "")
		}
	}

	return
}

func main() {
	fmt.Printf("getShortestPrefixes([\"dog\", \"cat\", \"apple\", \"apricot\", \"fish\"]) = %v", getShortestPrefixes([]string {"dog", "cat", "apple", "apricot", "fish"}))
}
