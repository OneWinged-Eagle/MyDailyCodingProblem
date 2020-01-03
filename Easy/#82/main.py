"""
Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.
"""

from typing import TextIO


def read7(f: TextIO) -> str:
	return f.read(7)


def readN(f: TextIO, n: int) -> str:
	read = readN.cache

	while len(read) < n:
		tmp = read7(f)
		if not tmp:
			readN.cache = ""
			return read

		read += tmp

	readN.cache = read[n:]

	return read[:n]


readN.cache = ""

f = open("./README.md", "r")
print(f"readN(f, 6) = {readN(f, 6)}")
print(f"readN(f, 6) = {readN(f, 6)}")
print(f"readN(f, 6) = {readN(f, 6)}")
print(f"readN(f, 6) = {readN(f, 6)}")
print(f"readN(f, 6) = {readN(f, 6)}")
print(f"readN(f, 6) = {readN(f, 6)}")
print(f"readN(f, 6) = {readN(f, 6)}")
print(f"readN(f, 6) = {readN(f, 6)}")
print(f"readN(f, 6) = {readN(f, 6)}")
print(f"readN(f, 6) = {readN(f, 6)}")
print(f"readN(f, 6) = {readN(f, 6)}")
print(f"readN(f, 6) = {readN(f, 6)}")
print(f"readN(f, 6) = {readN(f, 6)}")
print(f"readN(f, 6) = {readN(f, 6)}")
print(f"readN(f, 6) = {readN(f, 6)}")

f = open("./README.md", "r")
print(f"readN(f, 12) = {readN(f, 12)}")
print(f"readN(f, 12) = {readN(f, 12)}")
print(f"readN(f, 12) = {readN(f, 12)}")
print(f"readN(f, 12) = {readN(f, 12)}")
print(f"readN(f, 12) = {readN(f, 12)}")
print(f"readN(f, 12) = {readN(f, 12)}")
print(f"readN(f, 12) = {readN(f, 12)}")
print(f"readN(f, 12) = {readN(f, 12)}")
print(f"readN(f, 12) = {readN(f, 12)}")
