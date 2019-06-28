"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

# With r = 0.5, we have a circle of π/4 area.
# This 1 diameter circle can be enclosed inside a 1 area square (1x1).
# The ratio between the are of the square and the area of the circle is then π/4 / 1 = π/4.
# By taking a lot of random pairs of points (x, y), with x and y between 0 and 1, we have some points outside the circle and some points inside the circle.
# The points inside the circle are an approximation of its area, while the total of point are an approximation to the square area.
# We showed that circle_area / square_area = π/4, then numbers_of_points_inside_the_circle / total_numbers_of_points = π/4

from random import random


def estimatePi(nbRandomPoints: int) -> float:
	nbInCircle = 0

	for _ in range(nbRandomPoints):
		x = random()
		y = random()
		if x**2 + y**2 <= 1:
			nbInCircle += 1

	return round(4 * (nbInCircle / nbRandomPoints), 3)


print(f"estimatePi(10) = {estimatePi(10)}")
print(f"estimatePi(10) = {estimatePi(10)}")
print(f"estimatePi(10) = {estimatePi(10)}")
print(f"estimatePi(100) = {estimatePi(100)}")
print(f"estimatePi(100) = {estimatePi(100)}")
print(f"estimatePi(100) = {estimatePi(100)}")
print(f"estimatePi(1000) = {estimatePi(1000)}")
print(f"estimatePi(1000) = {estimatePi(1000)}")
print(f"estimatePi(1000) = {estimatePi(1000)}")
print(f"estimatePi(10000) = {estimatePi(10000)}")
print(f"estimatePi(10000) = {estimatePi(10000)}")
print(f"estimatePi(10000) = {estimatePi(10000)}")
print(f"estimatePi(100000) = {estimatePi(100000)}")
print(f"estimatePi(100000) = {estimatePi(100000)}")
print(f"estimatePi(100000) = {estimatePi(100000)}")
print(f"estimatePi(1000000) = {estimatePi(1000000)}")
print(f"estimatePi(1000000) = {estimatePi(1000000)}")
print(f"estimatePi(1000000) = {estimatePi(1000000)}")
