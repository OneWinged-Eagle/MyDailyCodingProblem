"""
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
"""

from enum import Enum
import re
from typing import List, Tuple


class Type(Enum):
	unknown = 0
	dir = 1
	file = 2


class Node:

	def __init__(self, name: str, type: Type):
		self.name = name
		self.type = type
		self.children = []


def getLongestPath(tree: Node) -> int:
	if tree.type == Type.file:
		return len(tree.name)

	elif tree.type == Type.dir:
		longestChildLength = 0

		for node in tree.children:
			childLength = getLongestPath(node)
			if childLength > longestChildLength:
				longestChildLength = childLength

		return longestChildLength + len(tree.name) if longestChildLength > 0 else 0

	elif tree.type == Type.unknown:
		return 0

	else:
		print("Unreachable code, exiting...")
		exit(-1)


def makeTree(leveledNodes: List[Tuple[int, Node]]) -> Node:
	if leveledNodes is None:
		return None

	currLevel = leveledNodes[0][0]
	currNode = leveledNodes[0][1]

	for i, (l, _) in enumerate(leveledNodes[1:]):
		if l <= currLevel:
			break
		if l == currLevel + 1:
			childNode = makeTree(leveledNodes[i + 1:])
			currNode.children.append(childNode)

	return currNode


def getType(name: str) -> Type:
	if re.search(r"\..+$", name) is not None:
		return Type.file
	elif name.find(".") == -1:
		return Type.dir
	return Type.unknown


def longestPath(fileSystem: str) -> int:
	splitLines = [lines.split("\t") for lines in fileSystem.split("\n")]
	leveledNodes = []

	for splitLine in splitLines:
		name = splitLine[-1]
		leveledNodes.append((len(splitLine) - 1, Node(name, getType(name))))

	fileSystemTree = makeTree(leveledNodes)

	return getLongestPath(fileSystemTree)


maxLen = longestPath("dir1\n\tsubdir1\n\tsubdir2")
print(f"longestPath(\"dir1\n\tsubdir1\n\tsubdir2\") = {maxLen}")

maxLen = longestPath("dir1\n\tsubdir1\n\tsubdir2\n\t\t.woah")
print(f"longestPath(\"dir1\n\tsubdir1\n\tsubdir2\n\t\t.woah\") = {maxLen}")

maxLen = longestPath("dir1\n\tsubdir1\n\t\tf.small\n\tsubdir2\n\t\tfile.big")
print(
    f"longestPath(\"dir1\n\tsubdir1\n\t\tf.small\n\tsubdir2\n\t\tfile.big\") = {maxLen}"
)

maxLen = longestPath("dir1\n\tsubdir1\n\t\tf.small\n\tsubdir2.\n\t\tfile.big")
print(
    f"longestPath(\"dir1\n\tsubdir1\n\t\tf.small\n\tsubdir2.\n\t\tfile.big\") = {maxLen}"
)

maxLen = longestPath(
    "dir1\n\tsubdir1\n\t\tf.small\n\t\tsubdir1subdir1\n\tsubdir2\n\t\tsubdir2subdir1\n\t\t\tfile.big"
)
print(
    f"longestPath(\"dir1\n\tsubdir1\n\t\tf.small\n\t\tsubdir1subdir1\n\tsubdir2\n\t\tsubdir2subdir1\n\t\t\tfile.big\") = {maxLen}"
)
