#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	# First convert into corrdinate points
	heightMap = {}
	for y, row in enumerate(data):
		for x, height in enumerate(row):
			heightMap[(x, y)] = int(height)
	
	# Now we find the points which is lower than its adjecent
	risk_sum = 0
	adjecent = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	for (x, y), height in heightMap.items():

		adj = []
		for dx, dy in adjecent:
			nx = x + dx
			ny = y + dy
			adj.append(heightMap.get((nx, ny), 9))
		
		if all(x > height for x in adj):
			risk_sum += height + 1

	return risk_sum

def part2(data):
	# First convert into corrdinate points
	heightMap = {}
	for y, row in enumerate(data):
		for x, height in enumerate(row):
			if height == '9': continue # we don't care about 9 as it will only slow us down
			heightMap[(x, y)] = int(height)
	
	# Now we find the points which is lower than its adjecent
	basinPoints = []
	adjecent = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	for (x, y), height in heightMap.items():

		adj = []
		for dx, dy in adjecent:
			nx = x + dx
			ny = y + dy
			adj.append(heightMap.get((nx, ny), 9))
		
		if all(x > height for x in adj):
			basinPoints.append((x, y))
	
	# Now we calculate the size of each basins
	sizes = []
	
	for point in basinPoints:
		
		explore = [point]
		explored = set()

		while len(explore) != 0:
			new_points = []
			for (x,y) in explore:
				for dx, dy in adjecent:
					nx = x + dx
					ny = y + dy
					if (nx, ny) in heightMap and (nx, ny) not in explored:
						new_points.append((nx, ny))
						explored.add((nx, ny))
			explore = new_points
		
		sizes.append(len(explored))

	sizes = sorted(sizes, reverse=True)
	return sizes[0] * sizes[1] * sizes[2]