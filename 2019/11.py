#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .intcode import computer5

split_data = ','
completed = True
raw_data = None # Not To be touched

def part1(data):
	direction_map = {
		0: (0, 1),
		1: (1, 0),
		2: (0, -1),
		3: (-1, 0)
	}
	direction = 0
	x, y = 0, 0
	panels = {} # key = (x, y), value = color (0 = black, 1 = white)
	computer = computer5.from_instructions(data)
	
	while not computer.halted:
		computer.input(panels.get((x, y), 0)) # Get color of current panel, or 0 if not painted
		color = computer.run_till_output()
		turn = computer.run_till_output()

		panels[(x, y)] = color # Paint panel
		direction = (direction + (1 if turn else -1)) % 4 # Turn
		# Move forward
		x += direction_map[direction][0]
		y += direction_map[direction][1]

	return len(panels)

def part2(data):
	direction_map = {
		0: (0, 1),
		1: (1, 0),
		2: (0, -1),
		3: (-1, 0)
	}
	direction = 0
	x, y = 0, 0
	panels = {(x, y): 1} # Starting panel is white
	computer = computer5.from_instructions(data)
	
	while not computer.halted:
		computer.input(panels.get((x, y), 0)) # Get color of current panel, or 0 if not painted
		color = computer.run_till_output()
		turn = computer.run_till_output()

		panels[(x, y)] = color # Paint panel
		direction = (direction + (1 if turn else -1)) % 4 # Turn
		# Move forward
		x += direction_map[direction][0]
		y += direction_map[direction][1]
	
	# Find min and max x and y
	min_x = min(panels, key=lambda k: k[0])[0]
	max_x = max(panels, key=lambda k: k[0])[0]
	min_y = min(panels, key=lambda k: k[1])[1]
	max_y = max(panels, key=lambda k: k[1])[1]

	# Print
	for y in range(max_y, min_y - 1, -1):
		for x in range(min_x, max_x + 1):
			print('\u2588' if panels.get((x, y), 0) else ' ', end='')
		print()
	
	print('This time, there will be no returned output as its super hard to guess all the letter patterns. However, a human can read the above display and figure out the output!')