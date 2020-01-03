"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""

from random import randrange


def rand5() -> int:
	return randrange(1, 6)


def rand7() -> int:
	target = 5 * rand5() + rand5()
	return (target % 7 + 1) if target <= 26 else rand7()


table140 = [0] * 7
for i in range(140):
	table140[rand7() - 1] += 1
print(f"table140 = {table140}")

table1400 = [0] * 7
for i in range(1400):
	table1400[rand7() - 1] += 1
print(f"table1400 = {table1400}")

table14000 = [0] * 7
for i in range(14000):
	table14000[rand7() - 1] += 1
print(f"table14000 = {table14000}")
