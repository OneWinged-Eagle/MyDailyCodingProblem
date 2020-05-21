"""
reduce (also known as fold) is a function that takes in an array, a combining function, and an initial value and builds up a result by calling the combining function on each element of the array, left to right. For example, we can write sum() in terms of reduce:

def add(a, b):
    return a + b

def sum(lst):
    return reduce(lst, add, 0)

This should call add on the initial value with the first element of the array, and then the result of that with the second element of the array, and so on until we reach the end, when we return the sum of the array.

Implement your own version of reduce.
"""

from typing import Any, Callable, List


def reduce(array: List[Any], func: Callable[[Any, Any], Any], init: Any) -> Any:
	val = init

	for n in array:
		val = func(val, n)

	return val


def add(a, b):
	return a + b


def mySum(lst):
	return reduce(lst, add, 0)


assert mySum([0, 0, 2, -2, 4, 8, 42, -4, -6, 10, -12]) == 42
print('passed')
