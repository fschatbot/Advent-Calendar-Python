#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


split_data = int
completed = True
raw_data = None # Not To be touched

# After completing this day, I found that the https://www.reddit.com/r/adventofcode/comments/a53r6i/comment/ebjosg2 also had a solution
# It was a bit more advanced, but I think it was better than my solution

def get_grid(serialNumber:int) -> np.array:
	grid = np.zeros((300, 300), dtype=int)

	# Calculating power for each cell
	for x in range(300):
		for y in range(300):
			rackID = x + 1 + 10
			power = rackID
			power *= (y + 1)
			power += serialNumber
			power *= rackID
			power = power // 100 % 10 # This will give us the hundreds digit
			power -= 5
			grid[y, x] = power
	
	return grid

def part1(data):
	grid = get_grid(int(data))
	
	# Finding 3x3 square with highest power
	max_power = 0
	max_x = 0
	max_y = 0
	for x in range(300 - 2):
		for y in range(300 - 2):
			Tpower = grid[y:y+3, x:x+3].sum()
			if max_power < Tpower:
				max_power = Tpower
				max_x = x
				max_y = y
	return f"{max_x + 1},{max_y + 1}"
	
def part2(data):
	grid = get_grid(int(data))
	
	# Finding 3x3 square with highest power
	max_power = 0
	max_x = 0
	max_y = 0
	max_size = 0
	for size in range(1, 301):
		for x in range(300 - (size - 1)):
			for y in range(300 - (size - 1)):
				Tpower = grid[y:y+size, x:x+size].sum()
				if max_power < Tpower:
					max_power = Tpower
					max_x = x
					max_y = y
					max_size = size
	return f"{max_x + 1},{max_y + 1},{max_size}"