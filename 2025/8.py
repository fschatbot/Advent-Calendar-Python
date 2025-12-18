#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	# First we create the distance matrix...
	distance_map = {}
	for i1 in range(len(data)):
		for i2 in range(i1 + 1, len(data)):
			x1, y1, z1 = [int(x) for x in data[i1].split(',')]
			x2, y2, z2 = [int(x) for x in data[i2].split(',')]
			distance_map[data[i1] + '|' + data[i2]] = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5
	
	
	circuits = [[junc] for junc in data] # These are the individual circuits...
	for key in sorted(distance_map.keys(), key=lambda x: distance_map[x])[:1000]:
		j1, j2 = key.split('|')
		i1, i2 = -1, -1
		for i in range(len(circuits)):
			if j1 in circuits[i]:
				i1 = i
			if j2 in circuits[i]:
				i2 = i
			if i1 != -1 and i2 != i2: break
		
		
		if i1 == i2: continue
		circuits[i1].extend(circuits[i2])
		circuits.pop(i2)
	

	count = sorted([len(cir) for cir in circuits], reverse=True)
	return count[0] * count[1] * count[2]

def part2(data):
	# First we create the distance matrix...
	distance_map = {}
	for i1 in range(len(data)):
		for i2 in range(i1 + 1, len(data)):
			x1, y1, z1 = [int(x) for x in data[i1].split(',')]
			x2, y2, z2 = [int(x) for x in data[i2].split(',')]
			distance_map[data[i1] + '|' + data[i2]] = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5
	
	
	circuits = [[junc] for junc in data] # These are the individual circuits...
	for key in sorted(distance_map.keys(), key=lambda x: distance_map[x]):
		j1, j2 = key.split('|')
		i1, i2 = -1, -1
		for i in range(len(circuits)):
			if j1 in circuits[i]:
				i1 = i
			if j2 in circuits[i]:
				i2 = i
			if i1 != -1 and i2 != i2: break
		
		
		if i1 == i2: continue
		circuits[i1].extend(circuits[i2])
		circuits.pop(i2)

		if len(circuits) == 1:
			return int(j1.split(',')[0]) * int(j2.split(',')[0])
	
	return None