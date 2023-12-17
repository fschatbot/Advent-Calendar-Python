#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
from itertools import combinations

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data:List[str]):
	mx, my = len(data[0]), len(data)
	new_data = []

	# Expanding the rows
	for line in data:
		new_data.append(line)
		if line.count('#') == 0:
			new_data.append(line)

	# Expanding the columns
	new_new_data = [''] * len(new_data)
	for col in range(mx):
		isEmpty = all(line[col] == '.' for line in new_data)
		for i, l in enumerate(new_data):
			new_new_data[i] += l[col]
			if isEmpty:
				new_new_data[i] += '.'
	
	# Finding all the pairs
	galaxies = []
	for y, l in enumerate(new_new_data):
		for x, char in enumerate(l):
			if char == '#':
				galaxies.append((x, y))
	
	# print(f"{len(galaxies)} Galaxies | {len(galaxies) * (len(galaxies) - 1) // 2} pairs ")

	acc = 0
	for p1, p2 in combinations(galaxies, 2):
		acc += abs(p2[0]-p1[0])+abs(p2[1]-p1[1])
	return acc

def part2(data:List[str]):
	mx, my = len(data[0]), len(data)

	# Instead of expanding the actual map, we instead take note of all the empty lines
	# Then we check if the line ever comes between two plannets and then do the calculation accordingly!

	empty_rows = []
	for i, line in enumerate(data):
		if line.count('#') == 0:
			empty_rows.append(i)
	
	empty_cols = []
	for col in range(mx):
		if all(line[col] == '.' for line in data):
			empty_cols.append(col)
	
	# Finding all the pairs
	galaxies = []
	for y, l in enumerate(data):
		for x, char in enumerate(l):
			if char == '#':
				galaxies.append((x, y))
	
	# print(f"{len(empty_rows)} empty rows | {len(empty_cols)} empty columns | {len(galaxies)} Galaxies | {len(galaxies) * (len(galaxies) - 1) // 2} pairs ")

	acc = 0
	for p1, p2 in combinations(galaxies, 2):
		hy = max(p2[1], p1[1])
		ly = min(p2[1], p1[1])
		hx = max(p2[0], p1[0])
		lx = min(p2[0], p1[0])

		for r in empty_rows:
			if ly < r < hy:
				acc += 999999 # 1 mil - 1
		for c in empty_cols:
			if lx < c < hx:
				acc += 999999  # 1 mil - 1
		acc += abs(p2[0]-p1[0]) + abs(p2[1]-p1[1])
	return acc