#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parser(data):
	row = []
	for line in data.split('\n'):
		row.append([c for c in line])
	
	return row

split_data = parser
completed = True
raw_data = None # Not To be touched

mov = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]

def part1(data):
	counter = 0
	for y in range(len(data)):
		for x in range(len(data[y])):
			if data[y][x] != '@': continue
			c = 0
			for dx, dy in mov:
				nx, ny = x + dx, y + dy
				if 0 <= nx < len(data[y]) and 0 <= ny < len(data) and data[ny][nx] == '@':
					c += 1
				if c >= 4: break
			else:
				counter += 1
	
	return counter

def part2(data):
	counter = 0
	
	removed = True
	while removed:
		removed = False
		for y in range(len(data)):
			for x in range(len(data[y])):
				if data[y][x] != '@': continue
				c = 0
				for dx, dy in mov:
					nx, ny = x + dx, y + dy
					if 0 <= nx < len(data[y]) and 0 <= ny < len(data) and data[ny][nx] == '@':
						c += 1
					if c >= 4: break
				else:
					data[y][x] = '.'
					counter += 1
					removed = True
	
	return counter
