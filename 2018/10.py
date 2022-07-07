#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	# Parsing the data and extracting information about each point
	line_parser = re.compile(r'position=<([\d\s-]+),([\d\s-]+)> velocity=<([\d\s-]+),([\d\s-]+)>')
	lines = []
	for line in data:
		m = line_parser.match(line)
		x, y, dx, dy = map(int, m.groups())
		lines.append({"posX": x, "posY":y, "velX": dx, "velY": dy})

	# Finding the smallest score and the points with that score
	score = 999999
	scoreS = None
	scoreP = None
	for second in range(20_000):
		# Calculating point position at each second
		points = []
		for line in lines:
			x = line['posX'] + (line['velX'] * second)
			y = line['posY'] + (line['velY'] * second)
			points.append((x, y))
		
		# The idea of founding the smallest bounding box is from:
		# https://www.reddit.com/r/adventofcode/comments/a4skra/comment/ebhafz0
		# finding the bounding box of the points
		min_x = min(points, key=lambda x: x[0])[0]
		max_x = max(points, key=lambda x: x[0])[0]
		min_y = min(points, key=lambda x: x[1])[1]
		max_y = max(points, key=lambda x: x[1])[1]

		# Finding the smallest bounding box
		bbox_size = (max_x - min_x) * (max_y - min_y)
		if bbox_size < score:
			score = bbox_size
			scoreS = second
			scoreP = points
	
	# Now we simply print the bounding box
	min_x = min(scoreP, key=lambda x: x[0])[0]
	max_x = max(scoreP, key=lambda x: x[0])[0]
	min_y = min(scoreP, key=lambda x: x[1])[1]
	max_y = max(scoreP, key=lambda x: x[1])[1]
	for y in range(min_y, max_y+1):
		for x in range(min_x, max_x+1):
			if (x, y) in scoreP:
				print('\u2588', end='')
			else:
				print(' ', end='')
		print()
	
	print('This time, there will be no returned output as its super hard to guess all the letter patterns. However, a human can read the above display and figure out the output!')

def part2(data):
	# Parsing the data and extracting information about each point
	line_parser = re.compile(r'position=<([\d\s-]+),([\d\s-]+)> velocity=<([\d\s-]+),([\d\s-]+)>')
	lines = []
	for line in data:
		m = line_parser.match(line)
		x, y, dx, dy = map(int, m.groups())
		lines.append({"posX": x, "posY":y, "velX": dx, "velY": dy})

	# Finding the smallest score and the points with that score
	score = 999999
	scoreS = None
	for second in range(20_000):
		# Calculating point position at each second
		points = []
		for line in lines:
			x = line['posX'] + (line['velX'] * second)
			y = line['posY'] + (line['velY'] * second)
			points.append((x, y))
		
		# The idea of founding the smallest bounding box is from:
		# https://www.reddit.com/r/adventofcode/comments/a4skra/comment/ebhafz0
		# finding the bounding box of the points
		min_x = min(points, key=lambda x: x[0])[0]
		max_x = max(points, key=lambda x: x[0])[0]
		min_y = min(points, key=lambda x: x[1])[1]
		max_y = max(points, key=lambda x: x[1])[1]

		# Finding the smallest bounding box
		bbox_size = (max_x - min_x) * (max_y - min_y)
		if bbox_size < score:
			score = bbox_size
			scoreS = second
	
	return scoreS