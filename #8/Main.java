
/*
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
*/

class Node {
	int val;
	Node left;
	Node right;

	public Node(int val, Node left, Node right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}

	public Node(int val, Node left) {
		this(val, left, null);
	}

	public Node(int val) {
		this(val, null, null);
	}

	public String toString() {
		return "Node(" + Integer.toString(this.val) + ")";
	}
}

public class Main {
	static boolean isUnivalTree(Node root) {
		if (root == null) {
			return true;
		}

		if (isUnivalTree(root.left) && isUnivalTree(root.right)) {
			if (root.left != null && root.left.val != root.val || root.right != null && root.right.val != root.val) {
				return false;
			}
			return true;
		}
		return false;
	}

	static int nbUnivalTrees(Node root) {
		if (root == null) {
			return 0;
		}
		return (isUnivalTree(root) ? 1 : 0) + nbUnivalTrees(root.left) + nbUnivalTrees(root.right);
	}

	public static void main(String[] args) {
		Node tree1111111 = new Node(1, new Node(1, new Node(1), new Node(1)), new Node(1, new Node(1), new Node(1)));
		System.out.printf("isUnivalTree(tree1111111) = %b%n", isUnivalTree(tree1111111));
		System.out.printf("nbUnivalTrees(tree1111111) = %d%n", nbUnivalTrees(tree1111111));

		Node tree1110101 = new Node(1, new Node(1, new Node(1), new Node(0)), new Node(1, new Node(0), new Node(1)));
		System.out.printf("isUnivalTree(tree1110101) = %b%n", isUnivalTree(tree1110101));
		System.out.printf("nbUnivalTrees(tree1110101) = %d%n", nbUnivalTrees(tree1110101));

		Node tree111null1null1 = new Node(1, new Node(1, new Node(1)), new Node(1, null, new Node(1)));
		System.out.printf("isUnivalTree(tree111null1null1) = %b%n", isUnivalTree(tree111null1null1));
		System.out.printf("nbUnivalTrees(tree111null1null1) = %d%n", nbUnivalTrees(tree111null1null1));
	}
}
