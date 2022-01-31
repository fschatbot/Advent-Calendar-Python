import numpy as np
split_data = True
completed = True
raw_data = None # Not To be touched

grid_shape = (100, 100)

def find_neigbors(grid, row, col):
	neighbors = 0
	for i in range(-1, 2): # -1, 0, 1
		for j in range(-1, 2): # -1, 0, 1
			if i == 0 and j == 0:
				# This is the original cell something we are not looking for
				continue
			elif row+i < 0 or row+i >= grid_shape[0]:
				# We are out of bounds
				continue
			elif col+j < 0 or col+j >= grid_shape[1]:
				# We are out of bounds
				continue
			else:
				try:
					neighbors += int(grid[row+i][col+j])
				except IndexError:
					# We are out of bounds
					continue
	return neighbors

def grid_str(grid):
	return '\n'.join([''.join(['#' if cell else '.' for cell in row]) for row in grid])

def generate_grid(data):
	grid = np.zeros(grid_shape, dtype=bool)
	for row in range(len(data)):
		for col in range(len(data[0])):
			if data[row][col] == '#':
				grid[row, col] = True
	return grid

def part1(data):
	# First we make our grid according to the data
	grid = generate_grid(data)
	# Now we have to go though 100 steps
	for _ in range(100):
		# First we make a new grid
		new_grid = np.zeros(grid_shape, np.bool)
		# Next we loop though the grid lights
		for row in range(grid_shape[0]):
			for col in range(grid_shape[1]):
				# We check the number of neighbors
				neighbors = find_neigbors(grid, row, col)
				state = grid[row, col]
				if state == True and neighbors in (2, 3):
					new_grid[row, col] = True
				elif state == False and neighbors == 3:
					new_grid[row, col] = True
		# Set the new grid to the old grid, update counter
		grid = new_grid
		print(_,end='\r')
	return np.sum(grid)

def part2(data):
	# Almost the same as part 1 but we have to add an expection for the 4 cornors
	# First we make our grid according to the data
	grid = generate_grid(data)
	# Set the 4 cornors to True
	# Found this cool hack on stackoverflow, https://stackoverflow.com/a/17937903/13703806
	grid[::grid_shape[0]-1, ::grid_shape[1]-1] = True
	# Now we have to go though 100 steps
	for _ in range(100):
		# First we make a new grid
		new_grid = np.zeros(grid_shape, np.bool)
		# Next we loop though the grid lights
		for row in range(grid_shape[0]):
			for col in range(grid_shape[1]):
				# Make sure the cornor lights are always on
				if row in (0, grid_shape[0]-1) and col in (0, grid_shape[1]-1):
					new_grid[row, col] = True
					continue
				# We check the number of neighbors
				neighbors = find_neigbors(grid, row, col)
				state = grid[row, col]
				# Apply the rules
				if state == True and neighbors in (2, 3):
					new_grid[row, col] = True
				elif state == False and neighbors == 3:
					new_grid[row, col] = True
		# Set the new grid to the old grid, update counter
		grid = new_grid
		print(_,end='\r')
	return np.sum(grid)

# THIS ONE WAS A LOT OF WORK