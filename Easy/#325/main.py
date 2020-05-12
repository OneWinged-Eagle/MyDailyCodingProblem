"""
The United States uses the imperial system of weights and measures, which means that there are many different, seemingly arbitrary units to measure distance. There are 12 inches in a foot, 3 feet in a yard, 22 yards in a chain, and so on.

Create a data structure that can efficiently convert a certain quantity of one unit to the correct amount of any other unit. You should also allow for additional units to be added to the system.
"""

from typing import Dict, List, Set, Tuple


class Converter:
	rates: Dict[str, Dict[str, float]]

	def __init__(self):
		self.units = set()
		self.rates = dict()

	def add(self, rate: float, unit: str, to: str):
		if unit not in self.rates:
			self.rates[unit] = dict()

		if to not in self.rates:
			self.rates[to] = dict()

		self.rates[unit][to] = rate
		self.rates[to][unit] = 1 / rate

	def convert(self,
	            quantity: float,
	            unit: str,
	            to: str,
	            visited: Set[str] = set()) -> Tuple[float, bool]:
		if unit in self.rates and to in self.rates[unit]:
			return (quantity * self.rates[unit][to], True)

		for u, r in self.rates[unit].items():
			if u in visited:
				continue

			visited.add(u)

			res, ok = self.convert(quantity * r, u, to, visited)
			if ok:
				return (res, True)

			visited.remove(u)

		return (0, False)


converter = Converter()
converter.add(22, "chain", "yard")
converter.add(3, "yard", "foot")
converter.add(12, "foot", "inch")

print(converter.units)
print(converter.rates)

assert converter.convert(1, "foot", "inch", set()) == (12, True)
assert converter.convert(1, "yard", "inch", set()) == (36, True)
assert converter.convert(1, "chain", "inch", set()) == (792, True)
print("passed")
