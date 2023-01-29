from math import sqrt, floor
import numpy as np

split_data = False
completed = True
raw_data = None # Not To be touched

def part1(data):
	data = int(data)
	# I spent my weekend over this problem and I over-engineered my answer!
	# Instead of simulating the grid, I am calculating the answer using quadratics
	# So this is a more of a mathamatical solution than a computer solution
	# This solution is O(1) as its an instant solve no matter the number
	
	# Helper functions for solving and equating quadractics
	def doQuod(a, b, c, x):
		return (a * (x**2)) + (b * x) + c
	
	def solvQuod(a, b, c):
		return (-b + sqrt((b**2) - (4 * a * c))) / (2 * a)
	
	# I am using the quadratic formula to find the ring number that this number is in
	# The Formula was derived from the lowest numbers and largest numbers in each ring
	# 
	# Formulas:
	# 	-> 4x^2 - 4x + 2 for the lowest numbers
	# 	-> 4x^2 - 4x + 1 for the largest numbers (unneeded)
	# The x represents the ring number
	# Now we are going to find the ring our number is in, by using the small number formula
	
	

	# Equating it with the lowest number allows us to find which ring is the data is on
	# However, the output is decimal so we floor to get rid of it
	ring = floor(solvQuod(4, -4, 2 - data))

	# Next we find all the middles in the given ring
	# Formulas for of side middles in a ring:
	# 	-> 4x^2 - 3x + 1 for mid 1
	# 	-> 4x^2 - 1x + 1 for mid 2
	# 	-> 4x^2 + 1x + 1 for mid 3
	# 	-> 4x^2 + 3x + 1 for mid 4
	middles = doQuod(4, -3, 1, ring), doQuod(4, -1, 1, ring), doQuod(4, 1, 1, ring), doQuod(4, 3, 1, ring)
	
	# Next we find the closest distance from any of the middles
	distance_from_mid = min(abs(m - data) for m in middles) # This is O(1) because the list doesn't scale and its always 4

	return distance_from_mid + ring

def part2(data):
	data = int(data)

	# Most of the work and the logic was from https://stackoverflow.com/a/23707273/13703806
	from itertools import count
	from collections import namedtuple

	Step = namedtuple("Step", ["dx", "dy"])
	RIGHT = Step( 1, 0)
	DOWN = Step( 0, 1)
	LEFT = Step(-1, 0)
	UP  = Step( 0, -1)

	size = (1000, 1000)
	mid = size[0] // 2 - 1

	grid = np.zeros(size, dtype=int)
	grid[mid, mid] = 1

	def steps_from_center():
		for n in count(start=1):
			if n % 2:
				yield RIGHT
				for i in range(n):
					yield UP
				for i in range(n):
					yield LEFT
			else:
				yield LEFT
				for i in range(n):
					yield DOWN
				for i in range(n):
					yield RIGHT
	last = 0
	x, y = mid, mid

	def output(x, y):
		return grid[y-1:y+2,x-1:x+2].sum()


	for i, step in enumerate(steps_from_center(), start=2):
		if last >= data:
			return last
		else:
			x += step.dx
			y += step.dy
			last = output(x, y)
			grid[y][x] = last