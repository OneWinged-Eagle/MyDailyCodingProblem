"""
Given a pivot x, and a list lst, partition the list into three parts.

    The first part contains all elements in lst that are less than x
    The second part contains all elements in lst that are equal to x
    The third part contains all elements in lst that are larger than x

Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].
"""

from typing import Any, List


def partition(x: Any, lst: List[Any]) -> List[Any]:
	i, left, right = 0, 0, len(lst) - 1

	while i <= right:
		if lst[i] < x:
			lst[i], lst[left] = lst[left], lst[i]
			i += 1
			left += 1
		elif lst[i] > x:
			lst[i], lst[right] = lst[right], lst[i]
			right -= 1
		else:
			i += 1

	return lst


for i in range(3, 15):
	print(
	    f"partition({i}, [9, 12, 3, 5, 14, 10, 10]) = {partition(i, [9, 12, 3, 5, 14, 10, 10])}"
	)
