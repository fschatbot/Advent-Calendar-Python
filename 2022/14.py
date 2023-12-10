#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict

def parse(data):
	caveMap = {}

	for line in set(data.split('\n')): # Using set because for some reason some lines were duplicate in the real data
		coords = [[int(a) for a in pos.split(',')] for pos in line.split(' -> ')]
		for start, end in zip(coords[:-1], coords[1:]):
			for y in range(start[1], end[1]+(1 if end[1] >= start[1] else -1), 1 if end[1] >= start[1] else -1):
				for x in range(start[0], end[0]+(1 if end[0] >= start[0] else -1), 1 if end[0] >= start[0] else -1):
					caveMap[x, y] = '#'
	
	return caveMap

def prettyPrint(caveMap):
	lowestXLevel = min(pos[0] for pos in caveMap)
	highestXLevel = max(pos[0] for pos in caveMap)
	lowestYLevel = max(pos[1] for pos in caveMap)
	highestYLevel = min(pos[1] for pos in caveMap)

	for y in range(highestYLevel, lowestYLevel+1):
		line = ''
		for x in range(lowestXLevel, highestXLevel+1):
			line += caveMap.get((x, y), '.')
		print(line)


split_data = parse
completed = True
raw_data = None # Not To be touched

def part1(data:Dict[tuple, str]):		
	lowestYLevel = max(pos[1] for pos in data)

	restingSand = 0
	flowing = True
	while flowing: # Run till the one of the sand reaches the abyss line
		sx, sy = 500, 0
		while True: # Run till the sand has nowhere to go!
			if sy >= lowestYLevel:
				flowing = False
				break
			elif (sx, sy+1) not in data: # Move Down
				sy += 1
			elif (sx-1, sy+1) not in data: # Move Down-Left
				sx -= 1
				sy += 1
			elif (sx+1, sy+1) not in data: # Move Down-Right
				sx += 1
				sy += 1
			else:
				restingSand += 1
				data[sx, sy] = 'O'
				break
	# prettyPrint(data)
	return restingSand

def part2(data:Dict[tuple, str]):
	lowestYLevel = max(pos[1] for pos in data) + 2

	restingSand = 0
	while (500, 0) not in data: # Run till the one of the sand reaches the abyss line
		sx, sy = 500, 0
		while True: # Run till the sand has nowhere to go!
			if sy+1 == lowestYLevel: # Simulating the cave floor
				restingSand += 1
				data[sx, sy] = 'O'
				break
			elif (sx, sy+1) not in data: # Move Down
				sy += 1
			elif (sx-1, sy+1) not in data: # Move Down-Left
				sx -= 1
				sy += 1
			elif (sx+1, sy+1) not in data: # Move Down-Right
				sx += 1
				sy += 1
			else:
				restingSand += 1
				data[sx, sy] = 'O'
				break
	# prettyPrint(data)
	return restingSand