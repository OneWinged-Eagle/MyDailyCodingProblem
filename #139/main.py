"""
Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface, which also implements peek(). peek shows the next element that would be returned on next().

Here is the interface:

class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
"""

from typing import Any, Iterator


class PeekableInterface:
	iterator: Iterator[Any]
	_next: Any

	def __init__(self, iterator: Iterator[Any]):
		self.iterator = iterator
		self._next = next(self.iterator, None)

	def peek(self) -> Any:
		return self._next

	def next(self) -> Any:
		ret = self._next
		self._next = next(self.iterator, None)
		return ret

	def hasNext(self):
		return self._next is not None


it = PeekableInterface(iter([1, 2, 3, 4, 5]))
assert it.peek() == 1
assert it.hasNext()
assert it.next() == 1
assert it.peek() == 2
assert it.hasNext()
assert it.next() == 2
assert it.peek() == 3
assert it.hasNext()
assert it.next() == 3
assert it.peek() == 4
assert it.hasNext()
assert it.next() == 4
assert it.peek() == 5
assert it.hasNext()
assert it.next() == 5
assert it.peek() == None
assert not it.hasNext()
assert it.next() == None
assert it.peek() == None
assert not it.hasNext()
assert it.next() == None
print("passed")
