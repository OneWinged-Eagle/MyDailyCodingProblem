"""
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).
"""

from random import randint


def rand7() -> int:
	return randint(1, 7)


def rand5() -> int:
	target = rand7()
	return target if target <= 5 else rand5()


table100 = [0] * 5
for i in range(100):
	table100[rand5() - 1] += 1
print(f"table100 = {table100}")

table1000 = [0] * 5
for i in range(1000):
	table1000[rand5() - 1] += 1
print(f"table1000 = {table1000}")

table10000 = [0] * 5
for i in range(10000):
	table10000[rand5() - 1] += 1
print(f"table10000 = {table10000}")

table100000 = [0] * 5
for i in range(100000):
	table100000[rand5() - 1] += 1
print(f"table100000 = {table100000}")
