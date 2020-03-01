package main

/*
Given a binary tree, determine whether or not it is height-balanced. A height-balanced binary tree can be defined as one in which the heights of the two subtrees of any node never differ by more than one.
*/

import "fmt"

func abs(nb int) uint {
	if nb < 0 {
		return uint(nb * -1)
	}

	return uint(nb)
}

func max(a, b int) int {
	if a < b {
		return b
	}

	return a
}

func height(root *node) int {
	if root == nil {
		return 0
	}

	return 1 + max(height(root.left), height(root.right))
}

func isBalanced(root *node) bool {
	if root == nil {
		return true
	}

	return abs(height(root.left)-height(root.right)) <= 1
}

func main() {
	root := newNode(nil, nil)
	fmt.Println("isBalanced(root) =", isBalanced(root))

	root.left = newNode(newNode(nil, nil), newNode(nil, nil))
	fmt.Println("isBalanced(root) =", isBalanced(root))
	fmt.Println("isBalanced(root.left) =", isBalanced(root.left))

	root.right = newNode(newNode(nil, nil), newNode(nil, nil))
	fmt.Println("isBalanced(root) =", isBalanced(root))
	fmt.Println("isBalanced(root.right) =", isBalanced(root.right))
}
