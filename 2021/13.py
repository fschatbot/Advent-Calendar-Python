#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = '\n\n'
completed = True
raw_data = None # Not To be touched

def print_points(points):
	points = set(tuple(point) for point in points)
	colLen = max(point[1] for point in points)
	rowLen = max(point[0] for point in points)

	for y in range(colLen+1):
		for x in range(rowLen+1):
			print('\u2588' if (x,y) in points else ' ', end='')
		print()
	
def part1(data):
	# This is just basic reflection (simple geomertic maths)
	 
	points, folding = data
	points = [[int(coord) for coord in point.split(',')] for point in points.split('\n')]
	
	fold = folding.split('\n')[0]
	modificationIndex = 0 if 'x' in fold else 1
	num = int(fold.split('=')[1])
	for point in points:
		if point[modificationIndex] < num: continue
		point[modificationIndex] = -point[modificationIndex] + 2 * num
	
	points = set(tuple(point) for point in points) # Remove any overlapping points
	return len(points)

def part2(data):
	# This is just basic reflection (simple geomertic maths)
	 
	points, folding = data
	points = [[int(coord) for coord in point.split(',')] for point in points.split('\n')]
	
	for fold in folding.split('\n'):
		modificationIndex = 0 if 'x' in fold else 1
		num = int(fold.split('=')[1])
		for point in points:
			if point[modificationIndex] < num: continue # Don't reflect anything that isn't going to change
			point[modificationIndex] = -point[modificationIndex] + 2 * num # Basic math equation for reflection
	
	points = set(tuple(point) for point in points) # Remove any overlapping points
	
	print_points(points)
	
	print('This time, there will be no returned output as its super hard to guess all the letter patterns. However, a human can read the above display and figure out the output!')