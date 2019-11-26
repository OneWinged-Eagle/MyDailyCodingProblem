package main

/*
Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

    There is 1 smaller element to the right of 3
    There is 1 smaller element to the right of 4
    There are 2 smaller elements to the right of 9
    There is 1 smaller element to the right of 6
    There are no smaller elements to the right of 1
*/

import "fmt"

func max(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

type Node struct {
	key    int
	left   *Node
	right  *Node
	height int

	size int
}

func newNode(key int) *Node {
	return &Node{key: key, height: 1, size: 1}
}

func height(node *Node) int {
	if node != nil {
		return node.height
	}

	return 0
}

func size(node *Node) int {
	if node != nil {
		return node.size
	}

	return 0
}

func (node *Node) update() {
	node.height = max(height(node.left), height(node.right)) + 1
	node.size = size(node.left) + size(node.right) + 1
}

func (node *Node) rightRotate() {
	left := node.left

	left.right, node.left = node, left.right

	node.update()
	left.update()

	node = left
}

func (node *Node) leftRotate() {
	right := node.right

	right.left, node.right = node, right.left

	node.update()
	right.update()

	node = right
}

func (node *Node) balance() int {
	return height(node.left) - height(node.right)
}

type BST struct {
	head *Node
}

func (bst *BST) add(key int) (count int) {
	if bst.head == nil {
		bst.head = newNode(key)
		return
	}

	curr := bst.head

	for true {
		if key < curr.key {
			if curr.left != nil {
				curr = curr.left
			} else {
				curr.left = newNode(key)
				break
			}
		} else {
			count += size(curr.left) + 1
			if curr.right != nil {
				curr = curr.right
			} else {
				curr.right = newNode(key)
				break
			}
		}
	}

	curr.update()

	balance := curr.balance()

	if balance > 1 && key < curr.left.key {
		curr.rightRotate()
	}

	if balance < -1 && key > curr.right.key {
		curr.leftRotate()
	}

	if balance > 1 && key > curr.left.key {
		curr.left.leftRotate()
		curr.rightRotate()
	}

	if balance < -1 && key < curr.right.key {
		curr.right.rightRotate()
		curr.leftRotate()
	}

	return
}

func reverse(elements []int) (reversed []int) {
	for i := len(elements) - 1; i >= 0; i-- {
		reversed = append(reversed, elements[i])
	}

	return
}

func smallerRightElements(elements []int) (smaller []int) {
	bst := &BST{}

	for _, elem := range reverse(elements) {
		smaller = append([]int{bst.add(elem)}, smaller...)
	}

	return
}

func main() {
	fmt.Printf("smallerRightElements([3, 4, 9, 6, 1]) = %v", smallerRightElements([]int{3, 4, 9, 6, 1}))
}
