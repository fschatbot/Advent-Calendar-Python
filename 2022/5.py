#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def proccess_data(data):
	crates, instructions = data.split('\n\n')
	# First we will convert the crates into map arrays
	crates = crates.split('\n')
	 # Take the last line, remove all the space so only the numbers remain and take the last number
	lastCrateIndex = int(crates[-1].replace(' ', '')[-1])
	crateMap = {i+1:[] for i in range(lastCrateIndex)}
	for line in crates[:-1]:
		# Splitting the string every 4th character as each crate line is that long
		split = [line[i:i+4] for i in range(0, len(line), 4)]
		# Loop through the crates in that row and if there is crate then add it to the map
		for index, crate in enumerate(split, start=1):
			char = crate[1]
			if char != ' ':
				crateMap[index].append(char)
	return [crateMap, instructions.split('\n')]

split_data = proccess_data
completed = True
raw_data = None # Not To be touched

def part1(data):
	crateMap, instructions = data
	# Now we follow the instructions
	for ins in instructions:
		move, fromCrate, toCrate = re.search(r"move (\d+) from (\d+) to (\d+)", ins).groups()
		move, fromCrate, toCrate = int(move), int(fromCrate), int(toCrate)
		# 0th index is the top
		# Hence remove the crate from the 0th index from the fromCrate and insert in 0th index in the toCrate
		for _ in range(move):
			item = crateMap[fromCrate].pop(0)
			crateMap[toCrate].insert(0, item)
	
	return ''.join(x[0] for x in crateMap.values())

def part2(data):
	crateMap, instructions = data
	# Now we follow the instructions
	for ins in instructions:
		move, fromCrate, toCrate = re.search(r"move (\d+) from (\d+) to (\d+)", ins).groups()
		move, fromCrate, toCrate = int(move), int(fromCrate), int(toCrate)

		items = [crateMap[fromCrate].pop(0) for _ in range(move)] # Get and remove the items from the start of fromCrate
		crateMap[toCrate] = items + crateMap[toCrate] # Add the items to the start in the toCrate
	
	return ''.join(x[0] for x in crateMap.values())
