#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	m, n = len(data), len(data[0])
	# We look for x and then see if it forms any XMAS
	# print(f"{m}x{n} grid")

	found = 0

	movements = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if (dx, dy) != (0, 0)]

	for y, line in enumerate(data):
		for x, char in enumerate(line):
			if char != 'X': continue

			for dx, dy in movements:
				nx, ny = x, y
				for i in range(3):
					nx, ny = nx + dx, ny + dy
					if not (0 <= nx < n and 0 <= ny < m): break
					if "MAS"[i] != data[ny][nx]: break # Checking if the ith letter is part of XMAS 
				else:
					found += 1

	return found

def part2(data):
	m, n = len(data), len(data[0])

	found = 0
	for y, line in enumerate(data):
		if not (1 <= y < m-1): continue
		for x, char in enumerate(line):
			if char != 'A': continue
			if not (1 <= x < n-1): continue

			for dx, dy in [(1, 1), (-1, 1)]:
				if set(["M", "S"]) != set([data[y+dy][x+dx], data[y-dy][x-dx]]):
					break
			else:
				found += 1
	
	return found
	