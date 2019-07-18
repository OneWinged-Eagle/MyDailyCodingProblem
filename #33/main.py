"""
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""

import heapq
from typing import List


class MinHeap:
	heap: List[int]

	def __init__(self):
		self.heap = []

	def push(self, val) -> None:
		heapq.heappush(self.heap, val)

	def pop(self) -> int:
		return heapq.heappop(self.heap)

	def __getitem__(self, i) -> int:
		return self.heap[i]

	def __len__(self) -> int:
		return len(self.heap)


class MaxHeap(MinHeap):

	def push(self, val) -> None:
		heapq.heappush(self.heap, -val)

	def pop(self) -> int:
		return -heapq.heappop(self.heap)

	def __getitem__(self, i) -> int:
		return -self.heap[i]


def median(stream: List[int]) -> None:
	if len(stream) == 0:
		return

	maxHeap = MaxHeap()
	minHeap = MinHeap()

	maxHeap.push(stream[0])
	print(stream[0])

	for nb in stream[1:]:
		if nb >= maxHeap[0]:
			minHeap.push(nb)
		else:
			maxHeap.push(nb)

		if len(maxHeap) > len(minHeap) + 1:
			minHeap.push(maxHeap.pop())
		elif len(minHeap) > len(maxHeap) + 1:
			maxHeap.push(minHeap.pop())

		if len(maxHeap) == len(minHeap):
			print((maxHeap[0] + minHeap[0]) / 2)
		elif len(maxHeap) > len(minHeap):
			print(maxHeap[0])
		else:
			print(minHeap[0])


print("median([2, 1, 5, 7, 2, 0, 5])...")
median([2, 1, 5, 7, 2, 0, 5])
print("median([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])...")
median([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
