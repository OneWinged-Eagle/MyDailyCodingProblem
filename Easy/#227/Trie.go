package main

type Node struct {
	word     string
	children map[rune]*Node
}

func newNode() *Node {
	return &Node{children: make(map[rune]*Node)}
}

type Trie struct {
	head *Node
}

func newTrie(dictionary set) *Trie {
	trie := &Trie{head: newNode()}

	for word := range dictionary {
		trie.insert(word)
	}

	return trie
}

func (t *Trie) insert(word string) {
	curr := t.head

	for _, char := range word {
		if _, ok := curr.children[char]; !ok {
			curr.children[char] = newNode()
		}
		curr = curr.children[char]
	}

	curr.word = word
}
