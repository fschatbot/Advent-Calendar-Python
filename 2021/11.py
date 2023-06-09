#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(data):
	map = {}
	for y, row in enumerate(data.split('\n')):
		for x, level in enumerate(row):
			map[(x, y)] = int(level)
	return map

split_data = parse
completed = True
raw_data = None # Not To be touched

adjecent = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)]

def part1(data):
	map = data
	flash = 0
	for _ in range(100):

		def increase(pos):
			if pos not in map: return 0
			map[pos] += 1
			if map[pos] == 10: # if flashed once
				yield 1
				for dx, dy in adjecent:
					nx, ny = pos[0] + dx, pos[1] + dy
					for output in increase((nx, ny)): yield output
			else:
				yield 0
		
		for point in map:
			for output in increase(point):
				flash += output
		
		# Now we reset any octopus above 9
		for point, value in map.items():
			if value > 9:
				map[point] = 0
	
	return flash

def part2(data):
	map = data
	step = 0
	
	def increase(pos):
		if pos not in map: return

		map[pos] += 1
		if map[pos] == 10: # if flashed once
			for dx, dy in adjecent:
				nx, ny = pos[0] + dx, pos[1] + dy
				increase((nx, ny))
	
	while not all(value == 0 for value in map.values()):
		step += 1

		for point in map:
			increase(point)

		# Now we reset any octopus above 9
		for point, value in map.items():
			if value > 9:
				map[point] = 0
	
	return step