#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	pos = 50
	counter = 0
	for line in data:
		d, t = line[:1], int(line[1:])
		pos += (1 if d == 'R' else -1) * t
		pos %= 100
		if pos == 0: counter += 1
	
	return counter

def part2(data):
	pos = 50
	counter = 0
	for line in data:
		d, t = line[:1], int(line[1:])
		for _ in range(t):
			pos += (1 if d == 'R' else -1)
			pos %= 100
			if pos == 0: counter += 1
	return counter