#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import re

split_data = True
completed = True
raw_data = None # Not To be touched

line_re = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

def proccess_line(line:str) -> dict:
	id, x, y, w, h = line_re.match(line).groups()
	return {
		'id': int(id),
		'x': int(x),
		'y': int(y),
		'w': int(w),
		'h': int(h)
	}

def part1(data):
	grid = np.zeros((1000, 1000), dtype=int)

	for line in data:
		line = proccess_line(line)

		# Increase the amount of claim of the square by each claim
		grid[line['x']:line['x']+line['w'], line['y']:line['y']+line['h']] += 1
	
	# Return a count of all the squares that have more than one claim
	return np.sum(grid > 1)
	

def part2(data):
	# We make our grid just like we did in part 1
	grid = np.zeros((1000, 1000), dtype=int)
	for line in data:
		line = proccess_line(line)
		grid[line['x']:line['x']+line['w'], line['y']:line['y']+line['h']] += 1
	
	# Loop through the grid and find the claim which has one throughtout it
	# We know that the claim is intact because it wasn't touched by any other claim
	for line in data:
		line = proccess_line(line)
		if np.all(grid[line['x']:line['x']+line['w'], line['y']:line['y']+line['h']] == 1):
			return line['id']