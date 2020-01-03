"""
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
"""

from typing import Any


class Log:

	def __init__(self):
		self.ordersIds = []

	# append is O(1) time complexity
	def record(self, order_id: int) -> None:
		self.ordersIds.append(order_id)

	# get item by index is O(1) time complexity
	def get_last(self, i: int) -> int:
		if 0 < i <= len(self.ordersIds):
			return self.ordersIds[i - 1]
		return None


log = Log()
log.record(1)
log.record(10)
log.record(42)
log.record(69)
log.record(420)
log.record(666)
log.record(1337)
print(f"log.get_last(0) = {log.get_last(0)}")
print(f"log.get_last(1) = {log.get_last(1)}")
print(f"log.get_last(2) = {log.get_last(2)}")
print(f"log.get_last(3) = {log.get_last(3)}")
print(f"log.get_last(4) = {log.get_last(4)}")
print(f"log.get_last(5) = {log.get_last(5)}")
print(f"log.get_last(6) = {log.get_last(6)}")
print(f"log.get_last(7) = {log.get_last(7)}")
print(f"log.get_last(8) = {log.get_last(8)}")

# I guess python is not the best language for this exercise, as lists are pretty optimised as if.
