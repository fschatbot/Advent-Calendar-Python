#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	grid = []
	for line in data:
		grid.append(re.sub(r'\s+', ' ', line).strip().split(' '))
	
	total = 0
	for p in range(len(grid[0])):
		if grid[-1][p] == '+':
			cu = sum(int(grid[x][p]) for x in range(len(grid)-1))
		else:
			cu = 1
			for x in range(len(grid)-1):
				cu *= int(grid[x][p])
		
		total += cu
	
	return total

def part2(data):
	# Could be solved better by simply transpossing the data...

	w, h = len(data[0]), len(data)
	problems = [{'nums': [], 'op': None}]
	for i in range(w):
		column = ''.join([data[j][i] for j in range(h)])
		if all(x == ' ' for x in column): # new problem...
			problems.append({'nums': [], 'op': None})
			continue

		if column[-1] != ' ': problems[-1]['op'] = column[-1]
		problems[-1]['nums'].append(int(column[:-1]))
	
	total = 0
	for problem in problems:
		if problem['op'] == '+':
			total += sum(problem['nums'])
		elif problem['op'] == '*':
			cu = 1
			for x in problem['nums']: cu *= x
			total += cu
		else:
			print(problem)
	
	return total