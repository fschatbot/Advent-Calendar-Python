#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def parse(data):
	grid = {}
	board, instructions = data.split('\n\n')

	for y, line in enumerate(board.split('\n')):
		for x, char in enumerate(line):
			if char == ' ': continue
			grid[(x, y)] = char	
	
	return grid, re.findall(r'\d+|L|R', instructions)

split_data = parse
completed = 1
raw_data = None # Not To be touched

def part1(data):
	grid, instructions = data
	# Super weird puzzle
	movements = [(1, 0), (0, 1), (-1, 0), (0, -1)] # Go right, down, left, up
	rotation = 0 # Starting out facing right

	# Find the start
	x, y = min(x for x, y in grid.keys() if y == 0), 0

	# print('We start at:', x, y, rotation)
	
	for op in instructions:
		if op == 'R':
			rotation = (rotation + 1) % 4
			continue
		elif op == 'L':
			rotation = (rotation - 1) % 4
			continue

		dx, dy = movements[rotation]
		# print("rot:", dx, dy, op)
		for _ in range(int(op)):
			nx, ny = x + dx, y + dy
			future = grid.get((nx, ny))
			if not future:
				# We can do this because of how the map looks. Special to only these kinds of map
				if rotation == 0:
					nx = min(gx for gx, gy in grid.keys() if gy == ny)
				elif rotation == 1:
					ny = min(gy for gx, gy in grid.keys() if gx == nx)
				elif rotation == 2:
					nx = max(gx for gx, gy in grid.keys() if gy == ny)
				elif rotation == 3:
					ny = max(gy for gx, gy in grid.keys() if gx == nx)
			future = grid.get((nx, ny))

			if future == '.':
				x, y = nx, ny # We move
			elif future == '#':
				break
	
	# print("We end at", x, y, rotation)

	return 1000 * (y+1) + 4 * (x+1) + (rotation % 4)

def part2(data):
	# HELL NO
	...