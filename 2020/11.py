#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(data):
	map = {}

	for y, line in enumerate(data.split('\n')):
		for x, state in enumerate(line):
			map[(x+1, y+1)] = state
	
	return map

split_data = parse
completed = True
raw_data = None # Not To be touched

def printSeats(map): 
	rowlen = max(pos[0] for pos in map.keys())
	collen = max(pos[1] for pos in map.keys())

	print()
	for y in range(1, collen + 1):
		for x in range(1, rowlen+1):
			print(map.get((x,y), '.'), end='')
		print()

# Relative coordinates for the adjecent squares
adj = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)]

def getAdjecent(coord, map):
	for (dx, dy) in adj:
		nx = coord[0] + dx
		ny = coord[1] + dy
		if map.get((nx, ny)) in ('L', '#'):
			yield map[(nx, ny)]

def part1(data):
	map = {}
	new_map = parse(data)
	while map != new_map:
		map, new_map = new_map, {}
		for pos, state in map.items():
			adjecents = [*getAdjecent(pos, map)]
			if state == 'L':
				new_map[pos] = '#' if adjecents.count('#') == 0 else 'L'
			elif state == '#':
				new_map[pos] = 'L' if adjecents.count('#') >= 4 else '#'
			else:
				new_map[pos] = state
	
	return sum(1 if state == '#' else 0 for state in map.values())
	
def getVisible(coord, map):
	for (dx, dy) in adj:
		nx = coord[0] + dx
		ny = coord[1] + dy

		# Keep going till we reach something
		while map.get((nx, ny)) == '.':
			nx, ny = nx + dx, ny + dy
		
		if map.get((nx, ny)) in ('L', '#'):
			yield map[(nx, ny)]

def part2(data):
	map = {}
	new_map = parse(data)
	while map != new_map:
		map, new_map = new_map, {}
		for pos, state in map.items():
			adjecents = [*getVisible(pos, map)]
			if state == 'L':
				new_map[pos] = '#' if adjecents.count('#') == 0 else 'L'
			elif state == '#':
				new_map[pos] = 'L' if adjecents.count('#') >= 5 else '#'
			else:
				new_map[pos] = state
		
	return sum(1 if state == '#' else 0 for state in map.values())