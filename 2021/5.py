#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	pipePoints = {}

	for line in data:
		start, end = line.split(' -> ')
		x1, y1 = start.split(',')
		x2, y2 = end.split(',')
		x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

		# Finding the direction of the pipe
		if x1 == x2: # horizontal
			smallY, BigY = (y1, y2) if y1 < y2 else (y2, y1)
			for y in range(smallY, BigY+1):
				if (x1, y) not in pipePoints: pipePoints[(x1, y)] = 0 
				pipePoints[(x1, y)] += 1
		elif y1 == y2: # Vertical
			smallX, BigX = (x1, x2) if x1 < x2 else (x2, x1)
			for x in range(smallX, BigX+1):
				if (x, y1) not in pipePoints: pipePoints[(x, y1)] = 0 
				pipePoints[(x, y1)] += 1

	# Counting the amount of points with overlaps
	return sum(1 for overlap in pipePoints.values() if overlap >= 2)

from itertools import cycle
def part2(data):
	pipePoints = {}

	for line in data:
		start, end = line.split(' -> ')
		x1, y1 = start.split(',')
		x2, y2 = end.split(',')
		x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

		# Calculating the x points of the pipe
		x_range = range(x1, x2+1) if x2 > x1 else range(x1, x2-1, -1)
		y_range = range(y1, y2+1) if y2 > y1 else range(y1, y2-1, -1)

		# Now we apply cycle to the shorter point range.
		# This will deal with the horizontal and veritcal pipes :)
		if len(x_range) < len(y_range): x_range = cycle(x_range)
		elif len(y_range) < len(x_range): y_range = cycle(y_range)
		
		# Now we simply mark those points in the pipePoint dataset
		for point in zip(x_range, y_range):
			if point not in pipePoints: pipePoints[point] = 0
			pipePoints[point] += 1
	
	# Counting the amount of points with overlaps
	return sum(1 for overlap in pipePoints.values() if overlap >= 2)