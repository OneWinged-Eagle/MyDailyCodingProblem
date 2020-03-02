package main

/*
In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7

You should return [1, 3, 2, 4, 5, 6, 7].
*/

import "fmt"

func boustrophedon(root *node) (numbers []int) {
	curr, next, left := stack{root}, stack{}, true

	for len(curr) > 0 {
		n := curr.pop()

		numbers = append(numbers, n.val)

		if left {
			if n.left != nil {
				next.push(n.left)
			}

			if n.right != nil {
				next.push(n.right)
			}
		} else {
			if n.right != nil {
				next.push(n.right)
			}

			if n.left != nil {
				next.push(n.left)
			}
		}

		if len(curr) == 0 {
			left = !left
			curr, next = next, curr
		}
	}

	return
}

func main() {
	root := newNode(1, newNode(2, newNode(4, nil, nil), newNode(5, nil, nil)), newNode(3, newNode(6, nil, nil), newNode(7, nil, nil)))
	fmt.Println("boustrophedon(root) =", boustrophedon(root))
}
