#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(data):
	# Converting to a 2D int array!
	return [[int(x) for x in line] for line in data.split('\n')]

split_data = parse
completed = True
raw_data = None # Not To be touched

def part1(data):
	movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]

	def calc_score(y0, x0):
		seen = set()
		queue = [(x0, y0)]
		score = 0

		while queue:
			x, y = queue.pop(0)

			for dx, dy in movement:
				nx, ny = x + dx, y + dy
				if not (0 <= nx < len(data[0]) and 0 <= ny < len(data)): continue # Out of bounds
				if data[ny][nx] - data[y][x] != 1: continue # Min increase of 1
				if f"{nx},{ny}" in seen: continue # Avoid repeats
				
				seen.add(f"{nx},{ny}")
				if data[ny][nx] == 9:
					score += 1
				else:
					queue.append((nx, ny))
		
		return score

	cum = 0
	for y, line in enumerate(data):
		for x, height in enumerate(line):
			if height != 0: continue
			cum += calc_score(y, x)

	
	return cum

def part2(data):
	movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]

	def calc_score(y0, x0):
		# Same stuff but removed the "seen" part! 
		queue = [(x0, y0)]
		score = 0

		while queue:
			x, y = queue.pop(0)

			for dx, dy in movement:
				nx, ny = x + dx, y + dy
				if not (0 <= nx < len(data[0]) and 0 <= ny < len(data)): continue # Out of bounds
				if data[ny][nx] - data[y][x] != 1: continue # Min increase of 1
				if data[ny][nx] == 9:
					score += 1
				else:
					queue.append((nx, ny))
		
		return score

	cum = 0
	for y, line in enumerate(data):
		for x, height in enumerate(line):
			if height != 0: continue
			cum += calc_score(y, x)

	
	return cum