#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .intersection import intersection

split_data = True
completed = 1
raw_data = None # Not To be touched

def part1(data):
	# Converting line data into points
	lines = []
	for line in data:
		coord = [0, 0]
		points = [coord.copy()]

		for ins in line.split(','):
			if ins.startswith('R'):
				coord[0] += int(ins[1:])
			elif ins.startswith('L'):
				coord[0] -= int(ins[1:])
			elif ins.startswith('U'):
				coord[1] += int(ins[1:])
			elif ins.startswith('D'):
				coord[1] -= int(ins[1:])
			points.append(coord.copy())
		
		lines.extend(zip(*points))
	
	inter_x, inter_y = intersection(*lines) # Finding all the intersections

	# Joining the 2 numpy arrays into a point list
	points = [*zip(inter_x, inter_y)]
	return min([abs(x) + abs(y) for x,y in points])

def part2(data):
	...