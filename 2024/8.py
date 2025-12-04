#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import combinations

def parse(data):
	ants = {}
	bounds = len(data.split('\n')[0]), len(data.split('\n'))
	for y, line in enumerate(data.split('\n')):
		for x, char in enumerate(line):
			if char == '.': continue
			if char not in ants: ants[char] = []
			ants[char].append((x, y))
	
	return ants, bounds

split_data = parse
completed = True
raw_data = None # Not To be touched

def part1(data):
	# Wow, this is pure math...
	ants, bounds = data
	antiNodes = set()
	for nodes in ants.values():

		for (a1x, a1y), (a2x, a2y) in combinations(nodes, r=2):
			dx, dy = a2x - a1x, a2y - a1y
			anti1 = (a1x - dx, a1y - dy)
			anti2 = (a2x + dx, a2y + dy)

			if 0 <= anti1[0] < bounds[0] and 0 <= anti1[1] < bounds[1]:
				antiNodes.add(anti1)
			if 0 <= anti2[0] < bounds[0] and 0 <= anti2[1] < bounds[1]:
				antiNodes.add(anti2)

	return len(antiNodes)

def part2(data):
	ants, bounds = data
	antiNodes = set()
	for nodes in ants.values():

		for (a1x, a1y), (a2x, a2y) in combinations(nodes, r=2):
			dx, dy = a2x - a1x, a2y - a1y

			nx, ny = a1x, a1y
			while 0 <= nx < bounds[0] and 0 <= ny < bounds[1]:
				antiNodes.add((nx, ny))
				nx -= dx
				ny -= dy
			
			nx, ny = a1x, a1y
			while 0 <= nx < bounds[0] and 0 <= ny < bounds[1]:
				antiNodes.add((nx, ny))
				nx += dx
				ny += dy

	return len(antiNodes)