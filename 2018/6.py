#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	minX,minY,maxX,maxY = float('inf'),float('inf'),float('-inf'),float('-inf')
	points = []
	area = {}
	for line in data:
		x, y = line.split(',')
		x, y = int(x), int(y)
		points.append((x, y))
		area[(x,y)] = 0
		minX, minY, maxX, maxY = min(minX, x-1), min(minY, y-1), max(maxX, x+1), max(maxY, y+1)
	
	black_listed = set()
	# We can determine the inf ones if they touch the boundary points
	# We will keep track of the area...
	
	for x in range(minX, maxX + 1):
		for y in range(minY, maxY + 1):
			# Finding the closest point
			double_best = False
			best_point = None
			best_d = float('inf')
			for point in points:
				px, py = point
				dis = abs(px-x) + abs(py-y)
				if dis < best_d:
					double_best = False
					best_point = point
					best_d = dis
				elif dis == best_d:
					double_best = True
			
			# Now we deal with adding areas and blacklisting
			if double_best != True:
				area[best_point] += 1
			if x in (minX, maxX) or y in (minY, maxY): # We are dealing with a boarder point
				black_listed.add(best_point)
	
	# Now we find point with the greatest area
	best_area = 0
	for point in points:
		if point in black_listed: continue
		if area[point] > best_area:
			best_area = area[point]
	
	return best_area


def part2(data):
	minX,minY,maxX,maxY = float('inf'),float('inf'),float('-inf'),float('-inf')
	points = []
	for line in data:
		x, y = line.split(',')
		x, y = int(x), int(y)
		points.append((x, y))
		minX, minY, maxX, maxY = min(minX, x-1), min(minY, y-1), max(maxX, x+1), max(maxY, y+1)
	
	# We can determine the inf ones if they touch the boundary points
	# We will keep track of the area...
	
	region_area = 0
	for x in range(minX, maxX + 1):
		for y in range(minY, maxY + 1):
			# Finding the total cost
			cost = 0
			for point in points:
				px, py = point
				dis = abs(px-x) + abs(py-y)
				cost += dis
			
			if cost < 10000:
				region_area += 1
	
	return region_area