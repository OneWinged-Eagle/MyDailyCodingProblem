"""
You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

    init(arr, size): initialize with the original large array and size.
    set(i, val): updates index at i with val.
    get(i): gets the value at index i.
"""

from typing import Any, Dict, List


class SparseArray:
	arr: Dict[int, Any]

	def __init__(self):
		self.arr = dict()

	def init(self, arr: List[Any], size: int):
		for i in range(size):
			if arr[i] is not None:
				self.arr[i] = arr[i]

	def set(self, i: int, val: any):
		if val is not None:
			self.arr[i] = val

	def get(self, i: int) -> Any:
		return self.arr.get(i)

	def __repr__(self):
		return repr(self.arr)


a = [i if i % 2 == 0 else None for i in range(10)]
print(f"'bad' array = {a}")

arr = SparseArray()
arr.init(a, 10)
print(f"'good' array = {arr}")

print(f"arr.get(1) = {arr.get(1)}")
arr.set(1, 1)
print(f"arr.get(1) = {arr.get(1)}")
