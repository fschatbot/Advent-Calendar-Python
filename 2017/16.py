#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = ','
completed = True
raw_data = None # Not To be touched

def part1(data):
	line = [program for program in 'abcdefghijklmnop']
	for movement in data:
		if movement[0] == 's':
			spinCount = int(movement[1:])
			line = line[-spinCount:] + line[:-spinCount]
		elif movement[0] == 'x':
			p1, p2 = map(int, movement[1:].split('/'))
			line[p2], line[p1] = line[p1], line[p2]
		elif movement[0] == 'p':
			p1, p2 = map(line.index, movement[1:].split('/'))
			line[p2], line[p1] = line[p1], line[p2]
	return ''.join(line)

def part2(data):
	dance = [program for program in 'abcdefghijklmnop']
	seen = []

	for i in range(1_000_000_000):
		# Skipping if we have already done this dance
		if ''.join(dance) in seen:
			return ''.join(seen[1_000_000_000 % i])
		else:
			seen.append(''.join(dance))
		
		# Doing the entire dance
		for movement in data:
			if movement[0] == 's':
				spinCount = int(movement[1:])
				dance = dance[-spinCount:] + dance[:-spinCount]
			elif movement[0] == 'x':
				p1, p2 = map(int, movement[1:].split('/'))
				dance[p2], dance[p1] = dance[p1], dance[p2]
			elif movement[0] == 'p':
				p1, p2 = map(dance.index, movement[1:].split('/'))
				dance[p2], dance[p1] = dance[p1], dance[p2]

	return ''.join(dance)