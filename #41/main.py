"""
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.
"""

from typing import List, NamedTuple


class Flight(NamedTuple):
	origin: str
	destination: str

def helper(flights: List[Flight], itinerary: List[str]) -> List[str]:
	if not flights:
		return itinerary

	itineraries = []

	for i, flight in enumerate(flights):
		if flight.origin == itinerary[-1]:
			itineraries.append(helper(flights[:i] + flights[i + 1:], itinerary + [flight.destination]))

	if not itineraries:
		return None
	return min(itineraries)

def getItinerary(flights: List[Flight], start: str) -> List[str]:
	return helper(flights, [start])

print(
    f"itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL') = {getItinerary([Flight('SFO', 'HKO'), Flight('YYZ', 'SFO'), Flight('YUL', 'YYZ'), Flight('HKO', 'ORD')], 'YUL')}"
)
print(
    f"itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM') = {getItinerary([Flight('SFO', 'COM'), Flight('COM', 'YYZ')], 'COM')}"
)
print(
    f"itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A') = {getItinerary([Flight('A', 'B'), Flight('A', 'C'), Flight('B', 'C'), Flight('C', 'A')], 'A')}"
)
