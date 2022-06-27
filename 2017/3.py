from math import sqrt, floor
import numpy as np

split_data = False
completed = 1
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
	return
	data = int(data)
	# Because we can't create a infinite grid, we will simply create a big grid instead
	# Just to keep it simple, we will make it odd * odd
	# This will give it a center
	grid = np.zeros((1001, 1001))
	def set_value(x, y , value):
		# Done because of weird numpy indexing behavior
		grid[x-1:y-1] = value
	# Ok I am being honest, I have no clue as why this does not work. Numpy is weird!
	def get_neighbours(x, y):
		return grid[x-1:y-1].sum()
	set_value(500, 500, 1)

	grid1 = np.zeros((5,5), dtype=np.int)
	grid1 = np.ndarray(shape=(5,5), dtype=np.int)
	grid1[2:2] = 1
	print(grid1)
	x, y = 3, 3
	print(grid1[y+1:x+1, 0:1])