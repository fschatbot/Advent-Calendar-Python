#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = '\n\n'
completed = 1
raw_data = None # Not To be touched

def part1(data):
	locks = []
	keys = []
	for schematic in data:
		schematic = schematic.split('\n')
		if schematic[0][0] == '.': # Key
			heights = [0, 0, 0, 0, 0]
			for col in range(5):
				for row in range(5):
					if schematic[5-row][col] == '#':
						heights[col] += 1
					else:
						break
			keys.append(heights)
		else: # Lock
			heights = [0, 0, 0, 0, 0]
			for col in range(5):
				for row in range(5):
					if schematic[1+row][col] == '#':
						heights[col] += 1
					else:
						break
			locks.append(heights)

	fits = 0
	for lock in locks:
		for key in keys:
			for ch1, ch2 in zip(lock, key):
				if ch1 + ch2 > 5:
					break
			else:
				fits += 1
	
	return fits

def part2(data):
	...