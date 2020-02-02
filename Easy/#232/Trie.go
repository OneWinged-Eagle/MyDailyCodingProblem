package main

type Node struct {
	val      int
	sum      int
	children map[rune]*Node
}

func newNode(val, sum int) *Node {
	return &Node{val: val, sum: sum, children: make(map[rune]*Node)}
}

type Trie struct {
	head *Node
}

func newTrie() *Trie {
	return &Trie{head: newNode(0, 0)}
}

func (t *Trie) insert(word string, val int) {
	curr, diff := t.head, val-t.getVal(word)

	for _, char := range word {
		if _, ok := curr.children[char]; ok {
			curr.sum += diff
		} else {
			curr.children[char] = newNode(0, val)
		}
		curr = curr.children[char]
	}

	curr.val = val
	curr.sum += diff
}

func (t Trie) getNode(word string) *Node {
	curr := t.head

	for _, char := range word {
		if _, ok := curr.children[char]; !ok {
			return nil
		}

		curr = curr.children[char]
	}

	return curr
}

func (t Trie) getSum(word string) int {
	if node := t.getNode(word); node != nil {
		return node.sum
	}

	return 0
}

func (t Trie) getVal(word string) int {
	if node := t.getNode(word); node != nil {
		return node.val
	}

	return 0
}
