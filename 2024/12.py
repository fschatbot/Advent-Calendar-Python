#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(data):
	grid = {}
	bounds = len(data.split('\n')[0]), len(data.split('\n'))
	for y, line in enumerate(data.split('\n')):
		for x, char in enumerate(line):
			grid[(x, y)] = char
	
	return grid, bounds

split_data = parse
completed = 1
raw_data = None # Not To be touched

def part1(data):
	grid, bounds = data
	price = 0

	def fencing(anchor):
		x, y = anchor
		area = 1
		perimeter = 0
		patch = set([(x, y)])
		crop = grid[anchor]
		movement = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		queue = [anchor]

		while queue:
			x, y = queue.pop(0)
			for dx, dy in movement:
				nx, ny = x + dx, y + dy
				if not (0 <= nx < bounds[0] and 0 <= ny < bounds[1]):
					perimeter += 1 # The border at the edge of the map
				elif (nx, ny) in patch:
					continue # Already seen this
				elif grid[(nx, ny)] == crop:
					area += 1
					queue.append((nx, ny))
					patch.add((nx, ny))
				else:
					perimeter += 1
		
		return area, perimeter, patch
	
	seen = set()

	for y in range(bounds[1]):
		for x in range(bounds[0]):
			if (x, y) in seen: continue
			area, perimeter, patch = fencing((x, y))
			# print(f'A region of {grid[(x, y)]} plants with price {area} * {perimeter} = {area*perimeter}')
			seen.update(patch)
			price += area*perimeter

	return price

def part2(data):
	grid, bounds = data
	...