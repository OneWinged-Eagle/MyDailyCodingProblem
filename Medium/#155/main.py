"""
Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""

from typing import Any, List


def majElem(elements: List[Any]) -> Any:
	d = dict()

	for elem in elements:
		d[elem] = d.get(elem, 0) + 1

		if d[elem] > len(elements) // 2:
			return elem

	return None


assert majElem([1, 2, 1, 1, 3, 0, 1]) == 1
assert majElem([1, 2, 1, 1, 3, 4]) == None
assert majElem([1, 2, 1, 1, 3]) == 1
assert majElem([]) == None
print("passed")
