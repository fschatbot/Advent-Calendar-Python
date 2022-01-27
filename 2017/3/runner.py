from dis import dis
from math import sqrt, trunc

split_data = False
completed = False
raw_data = None # Not To be touched

def part1(data):
	data = int(data)
	# I spent my weekend over this problem and I over-engineered my answer!
	# Instead of simulating the grid, I am calculating the answer using quadratics
	# So this is a more of a mathamatical solution than a computer solution
	# 
	# I am using the quadratic formula to find the ring number that this number is in
	# The Formula was derived from the lowest numbers and largest numbers in each ring
	# 
	# Formulas:
	# 	-> 4x^2 - 11x + 8 for the lowest numbers
	# 	-> 4x^2 - 4x + 1 for the largest numbers
	# The x represents the ring number
	# Now we are going to find the ring our number is from using the small number formula
	
	a = 4
	b = -11
	c = 8 - data
	ring = (-b + sqrt((b**2) - (4 * a * c))) / (2 * a)
	# This will simply remove the unwanted decimals
	ring = trunc(ring)
	# How far our number is from the smallest number in the ring
	distance = data - ((4 * (ring**2)) - (11 * ring) + 8)
	# Now we somewhat do a simulation of the grid just to convert our distance to a grid position
	# This estially creates a array with numbers going up and down. Ex: 2, 3, 4, 3
	# This allows up to warp our distance in this list and return the corresponding distance from 0
	grid_layout = [*range(ring-1, 2*(ring-1)), *range(2*(ring-1), ring-1, -1)]
	# Now we simply warp the distance to the grid and return the answer
	return grid_layout[distance % len(grid_layout)]


	return ring

def part2(data):
	pass