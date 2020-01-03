"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

import threading


def jobScheduler(f, n):
	threading.Timer(n / 1000, f).start()


def functionPrintStuff(stuff):

	def printStuff():
		print(stuff)

	return printStuff


jobScheduler(functionPrintStuff("This is a test!"), 1000)
jobScheduler(functionPrintStuff("Hello World!"), 500)
jobScheduler(functionPrintStuff("SUCC"), 200)
