#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data) -> int:
	# Finding all the partNumbers with additional data: O(m * n)
	partList = []
	for y, line in enumerate(data):
		i = 0
		continuation = False
		while i < len(line):
			char = line[i]
			if char.isdigit() and continuation == False:
				continuation = True
				partList.append({'partId': char, 'length': 1, 'start': (i, y)})
			elif char.isdigit() and continuation == True:
				partList[-1]['partId'] += char
				partList[-1]['length'] += 1
			elif not char.isdigit() and continuation == True:
				continuation = False
			i += 1
	
	# Checking for symbols around the part
	acc = 0
	symbol = []
	for part in partList:
		found = False
		for y in range(part['start'][1] - 1, part['start'][1] + 2): # Up, mid, down
			if not (0 <= y < len(data)): continue # Staying inbound
			if found: break
			for x in range(part['start'][0] - 1, part['start'][0] + part['length'] + 1): # Left to right
				if not (0 <= x < len(data[0])): continue # Staying inbound
				if data[y][x].isdigit() or data[y][x] == '.': continue # Skip dots and numbers around the thing
				acc += int(part['partId']) # There is a symbol around
				symbol.append(data[y][x])
				found = True
				break
	return acc

def part2(data) -> int:	
	# Finding all the partNumbers with additional data: O(m * n)
	partList = []
	gearList = []
	for y, line in enumerate(data):
		i = 0
		continuation = False
		while i < len(line):
			char = line[i]
			if char.isdigit() and continuation == False:
				continuation = True
				partList.append({'partId': char, 'locs': [(i, y)]})
			elif char.isdigit() and continuation == True:
				partList[-1]['partId'] += char
				partList[-1]['locs'].append((i, y))
			elif not char.isdigit() and continuation == True:
				continuation = False
			if char == '*':
				gearList.append((i, y))
			i += 1
	
	# Finding all valid gear symbols
	acc = 0
	for gear in gearList:
		validPlacement = [(x, y) for y in range(gear[1]-1, gear[1]+2) for x in range(gear[0]-1, gear[0]+2) if (x, y) != gear and 0 <= y < len(data) and 0 <= x < len(data[0])]
		nearBy = [part['partId'] for part in partList if any(loc in validPlacement for loc in part['locs'])]
		if len(nearBy) != 2: continue
		acc += int(nearBy[0]) * int(nearBy[1])
	
	return acc