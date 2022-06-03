import re
import numpy as np

split_data = True
completed = True
raw_data = None # Not To be touched

def proccess_data(data):
	nodes = {}

	regex = re.compile(r"/dev/grid/node-x(\d+)-y(\d+)\s*(\d+)T\s*(\d+)T\s*(\d+)T\s*(\d+)%")

	for line in data[2:]:
		nx, ny, size, used, avail, perc = regex.match(line).groups()
		nodes[(int(nx), int(ny))] = {
			"size": int(size),
			"used": int(used),
			"avail": int(avail),
			"perc": int(perc)
		}
	
	return nodes

def part1(data):
	proccessed = proccess_data(data)
	# Finding all the pairs whose used space is less than the available space
	counter = 0
	for node in proccessed:
		for other in proccessed:
			if node != other and proccessed[node]["used"] != 0 and proccessed[node]["used"] <= proccessed[other]["avail"]:
				counter += 1
	# Now we have to remove all the duplicates
	return counter


def part2(data):
	proccessed = proccess_data(data)
	'''
	Here is a simple trick to solve this problem easily.
	Say we have a grid like so
	Grid 1:
	......G
	.......
	.######
	..._...

	The first thing that we need to do, is move the empty space(_) to the top left corner.
	Grid 2:
	_.....G
	.......
	.######
	.......

	Next we need to move the empty space(_) to G directly.
	Grid 3:
	.....G_
	.......
	.######
	.......

	It takes 5 steps to move the G left with the _ behind it
	Grid 4:
	....G_.
	.......
	.######
	.......
	
	So if we simply keep doing this until the G reaches the top left corner.
	We can define the number of steps it will take for G to reach top left if the empty space was at the top left corner with the following equation:
	maxX + 5(maxX - 1)
	where `maxX` is the maximum X coordinate of the grid.
	'''
	# Count the average number of node size
	c = 0
	for x in proccessed.values():
		c += x['size']
	avg = c/len(proccessed.values())

	# First we create the grid
	maxX = max(proccessed.keys(), key=lambda x: x[0])[0]
	maxY = max(proccessed.keys(), key=lambda x: x[1])[1]
	grid = np.zeros((maxX + 1, maxY + 1), dtype=int)

	# Then we fill it with the data
	# 1 is equal to wall, 0 is equal to empty space, -1 is equal to movable space
	for y in range(maxY + 1):
		for x in range(maxX + 1):
			node = proccessed[(x, y)]
			if node['size'] > avg:
				grid[x, y] = 1
			elif node["used"] == 0:
				ax, ay = x, y
				grid[x, y] = 0
			else:
				grid[x, y] = -1

	# Pretty printing the data
	with open("2016/day 22.dump.txt", "w") as f:
		# Printing the display into the console
		display = grid.astype(np.str)
		display[display == '1'] = '#'
		display[display == '0'] = '_'
		display[display == '-1'] = '.'
		lines = []
		for row in display.T:
			lines.append(' '.join(row))
		f.write('\n'.join(lines))
	
	# Now we need to find the shortest path from ax, ay to (maxX, 0)
	# We will use a BFS algorithm
	def bfs(queue, visited, dept):
		next_queue = [] # The next move to take
		for coord in queue: # For each coordinate in the queue
			for mx, my in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
				movement = coord[0] + mx, coord[1] + my
				if movement in visited or movement[0] < 0 or movement[1] < 0 or movement[0] >= maxX + 1 or movement[1] >= maxY + 1: continue
				elif movement == (maxX, 0): # If we are at the destination we are done
					return dept
				elif grid[movement] != 1:
					next_queue.append(movement)
					visited.append(movement)
		return bfs(next_queue, visited, dept+1)
	
	shortest_path = bfs([(ax, ay)], [(ax, ay)], 1)
	return 5 * (maxX - 1) + shortest_path

