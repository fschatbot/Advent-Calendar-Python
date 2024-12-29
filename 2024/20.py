#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(data):
	grid = []
	boundX, boundY = len(data.split('\n')[0]), len(data.split('\n'))
	start = None, None
	end = None, None
	for y, line in enumerate(data.split('\n')):
		for x, char in enumerate(line):
			if char == '#':
				grid.append((x, y))
			elif char == '.':
				pass
			elif char == 'S':
				start = x, y
			elif char == 'E':
				end = x, y
	
	return grid, (boundX, boundY), start, end

split_data = parse
completed = 1
raw_data = None # Not To be touched

def pathFinder(grid, start, end):
	# Simple greedy algo since there is only one path
	path = [start, start]
	directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
	while path[-1] != end:
		# print(path[-1])
		for dx, dy in directions:
			nx, ny = path[-1][0]+dx, path[-1][1]+dy
			if (nx, ny) in grid: continue
			if (nx, ny) == path[-2]: continue

			path.append((nx, ny))
			break
	
	return path[1:]


def part1(data):
	grid, bounds, start, end = data
	path = pathFinder(grid, start, end)

	moves = [(0, -2), (0, 2), (2, 0), (-2, 0)]

	counter = 0

	for i, (x, y) in enumerate(path):
		for dx, dy in moves:
			nx, ny = x + dx, y + dy
			if (nx, ny) not in path[i:]: continue
			save = path[i:].index((nx, ny)) - 2
			if save >= 100: counter += 1
	
	return counter

def part2(data):
	grid, bounds, start, end = data
	path = pathFinder(grid, start, end)

	# Some black magic is required over here cause the amount of checks look like 10k * 50**2 ~= 25 mill
	moves = [(0, -2), (0, 2), (2, 0), (-2, 0)]

	counter = 0

	for i, (x, y) in enumerate(path):
		for dx, dy in moves:
			nx, ny = x + dx, y + dy
			if (nx, ny) not in path[i:]: continue
			save = path[i:].index((nx, ny)) - 2
			if save >= 100: counter += 1
	
	return counter