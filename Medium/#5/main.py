"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
	def pair(f):
		return f(a, b)
	return pair

Implement car and cdr.
"""


def cons(a, b):

	def pair(f):
		return f(a, b)

	return pair


"""
First attempt, took the "pair" too literally

def make_pair(a, b):
	return (a, b)


def car(pair):
	return pair(make_pair)[0]


def cdr(pair):
	return pair(make_pair)[1]

"""


def car(f):
	return f(lambda a, b: a)


def cdr(f):
	return f(lambda a, b: b)


f1 = cons(3, 4)
print(f"car(cons(3, 4)) = {car(f1)}")
print(f"car(cons(3, 4)) = {cdr(f1)}")

f2 = cons(
    cons("first-first", "first-second"), cons("second-first", "second-second"))
print(
    f"car(car(cons(\"first-first\", \"first-second\"), cons(\"second-first\", \"second-second\"))) = {car(car(f2))}"
)
print(
    f"car(cdr(cons(\"first-first\", \"first-second\"), cons(\"second-first\", \"second-second\"))) = {car(cdr(f2))}"
)
print(
    f"cdr(car(cons(\"first-first\", \"first-second\"), cons(\"second-first\", \"second-second\"))) = {cdr(car(f2))}"
)
print(
    f"cdr(cdr(cons(\"first-first\", \"first-second\"), cons(\"second-first\", \"second-second\"))) = {cdr(cdr(f2))}"
)
