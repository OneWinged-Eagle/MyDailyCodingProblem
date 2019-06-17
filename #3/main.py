# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
# 	def __init__(self, val, left=None, right=None):
# 		self.val = val
# 		self.left = left
# 		self.right = right

# The following test should pass:

# node = Node("root", Node("left", Node("left.left")), Node("right"))
# assert deserialize(serialize(node)).left.left.val == "left.left"


class Node:

	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def recursiveDeserialise():
	val = None
	if len(recursiveDeserialise.vals) != 0:
		val = recursiveDeserialise.vals[0]
	else:
		return None

	recursiveDeserialise.vals = recursiveDeserialise.vals[1:]

	if val == "None":
		return None

	return Node(val, recursiveDeserialise(), recursiveDeserialise())


# time O(log n) (?), space O(n), can't use "None" as Node.val (and any strings with blank characters)
def deserialise(s):
	recursiveDeserialise.vals = s.split()
	return recursiveDeserialise()


# time O(log n) (?), space O(1), can't use "None" as Node.val (and any strings with blank characters)
def serialise(root):
	if root == None:
		return None
	return f"{root.val} {serialise(root.left)} {serialise(root.right)}"


node = Node("root", Node("left", Node("left.left")), Node("right"))
serialisedNode = serialise(node)
print(serialisedNode)
deserialisedNode = deserialise(serialisedNode)
assert deserialisedNode.left.left.val == "left.left"
assert deserialisedNode.right.val == "right"
print(serialise(deserialisedNode))

node = Node(0, Node("l", None, Node("lr")),
            Node("r", Node("rl", None, Node("rlr")), Node("rr")))
serialisedNode = serialise(node)
print(serialisedNode)
deserialisedNode = deserialise(serialisedNode)
assert deserialisedNode.left.right.val == "lr"
assert deserialisedNode.right.left.right.val == "rlr"
print(serialise(deserialisedNode))
