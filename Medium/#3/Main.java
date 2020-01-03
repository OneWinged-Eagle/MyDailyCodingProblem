
/*
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
 	def __init__(self, val, left=None, right=None):
 		self.val = val
 		self.left = left
 		self.right = right

The following test should pass:

node = Node("root", Node("left", Node("left.left")), Node("right"))
assert deserialize(serialize(node)).left.left.val == "left.left"
*/

import java.util.concurrent.atomic.AtomicInteger;

class Node {
	String val;
	Node left;
	Node right;

	public Node(String val, Node left, Node right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}

	public Node(String val, Node left) {
		this(val, left, null);
	}

	public Node(String val) {
		this(val, null, null);
	}

	public String toString() {
		return "Node(" + this.val + ")";
	}
}

public class Main {
	static Node deserialiseHelper(String[] nodes, AtomicInteger index) {
		if (index.get() >= nodes.length) {
			return null;
		}

		String val = nodes[index.getAndIncrement()];
		if (val.equals("null")) {
			return null;
		}

		return new Node(val, deserialiseHelper(nodes, index), deserialiseHelper(nodes, index));
	}

	static Node deserialise(String str) {
		return deserialiseHelper(str.split("\\s+"), new AtomicInteger(0));
	}

	static String serialise(Node node) {
		if (node == null) {
			return null;
		}

		return node.val + " " + serialise(node.left) + " " + serialise(node.right);
	}

	public static void main(String[] args) {
		Node node = new Node("root", new Node("left", new Node("left.left")), new Node("right"));
		String serialisedNode = serialise(node);
		System.out.printf("serialise(node) = %s%n", serialisedNode);
		Node deserialisedNode = deserialise(serialisedNode);
		System.out.printf("deserialisedNode.left.left = %s%n", deserialisedNode.left.left);
		System.out.printf("deserialisedNode.right = %s%n", deserialisedNode.right);
		System.out.printf("serialise(deserialisedNode) = %s%n", serialise(deserialisedNode));

		node = new Node("root", new Node("l", null, new Node("lr")),
				new Node("r", new Node("rl", null, new Node("rlr")), new Node("rr")));
		serialisedNode = serialise(node);
		System.out.printf("serialise(node) = %s%n", serialisedNode);
		deserialisedNode = deserialise(serialisedNode);
		System.out.printf("deserialisedNode.left.right = %s%n", deserialisedNode.left.right);
		System.out.printf("deserialisedNode.right.left.right = %s%n", deserialisedNode.right.left.right);
		System.out.printf("serialise(deserialisedNode) = %s%n", serialise(deserialisedNode));
	}
}
