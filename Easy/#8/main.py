"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""


class Node:

	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def isUnivalTree(node):
	if node is None:
		return True

	isLeftUnival = isUnivalTree(node.left)
	isRightUnival = isUnivalTree(node.right)

	if isLeftUnival and isRightUnival:
		if node.left is not None and node.left.val != node.val:
			return False
		if node.right is not None and node.right.val != node.val:
			return False
		return True
	return False


# time O(???), space O(1), need to add some caching
def nbUnivalTree(root):
	if root is None:
		return 0
	return isUnivalTree(root) + nbUnivalTree(root.left) + nbUnivalTree(root.right)


tree1111111 = Node(1, Node(1, Node(1), Node(1)), Node(1, Node(1), Node(1)))
print(f"isUnivalTree(tree1111111) = {isUnivalTree(tree1111111)}")
print(f"nbUnivalTree(tree1111111) = {nbUnivalTree(tree1111111)}")

tree1110101 = Node(1, Node(1, Node(1), Node(0)), Node(1, Node(0), Node(1)))
print(f"isUnivalTree(tree1110101) = {isUnivalTree(tree1110101)}")
print(f"nbUnivalTree(tree1110101) = {nbUnivalTree(tree1110101)}")

tree111None1None1 = Node(1, Node(1, Node(1), None), Node(1, None, Node(1)))
print(f"isUnivalTree(tree111None1None1) = {isUnivalTree(tree111None1None1)}")
print(f"nbUnivalTree(tree111None1None1) = {nbUnivalTree(tree111None1None1)}")
