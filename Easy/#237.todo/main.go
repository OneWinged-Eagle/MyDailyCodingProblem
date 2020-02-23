package main

/*
A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node. The following tree is an example:

        4
      / | \
    3   5   3
  /           \
9              9

Given a k-ary tree, determine whether it is symmetric.
*/

import "fmt"

func isSymmetric(root *Node) bool {
	start, end := 0, len(root.children)-1

	for start <= end {
		sNode, eNode := root.children[start], root.children[end]

		if start < end {
			if sNode.val != eNode.val || !sNode.equals(eNode.reverse()) {
				return false
			}
		} else {
			if !isSymmetric(sNode) {
				return false
			}
		}

		start++
		end--
	}

	return true
}

func main() {
	tree := &Node{4, []*Node{
		&Node{3, []*Node{
			&Node{9, nil},
		}},
		&Node{5, nil},
		&Node{3, []*Node{
			&Node{9, nil},
		}},
	}}
	fmt.Println("tree =", tree)
	fmt.Println("isSymmetric(tree) =", isSymmetric(tree))

	tree = &Node{4, []*Node{
		&Node{3, []*Node{
			&Node{9, nil},
		}},
		&Node{5, nil},
		&Node{5, nil},
		&Node{3, []*Node{
			&Node{9, nil},
		}},
	}}
	fmt.Println("tree =", tree)
	fmt.Println("isSymmetric(tree) =", isSymmetric(tree))

	tree = &Node{4, []*Node{
		&Node{3, []*Node{
			&Node{9, nil},
		}},
		&Node{5, nil},
		&Node{5, nil},
		&Node{3, []*Node{
			&Node{9, []*Node{&Node{2, nil}}},
		}},
	}}
	fmt.Println("tree =", tree)
	fmt.Println("isSymmetric(tree) =", isSymmetric(tree))
}
