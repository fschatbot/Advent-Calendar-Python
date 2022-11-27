#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Tuple

split_data = True
completed = True
raw_data = None # Not To be touched

def generateMapping(path) -> List[Tuple[int]]:
	"""Generates a list of coordinate points that the wire takes us to"""
	coord = [0, 0]
	points = []

	for ins in path.split(','):
		val = int(ins[1:])
		for _ in range(val):
			if ins.startswith('R'):
				coord[0] += 1
			elif ins.startswith('L'):
				coord[0] -= 1
			elif ins.startswith('U'):
				coord[1] += 1
			elif ins.startswith('D'):
				coord[1] -= 1
			points.append(tuple(coord))
	return points

def part1(data):
	# Converting line data into points
	wires = [generateMapping(wire) for wire in data]
	
	inter = set(wires[0]).intersection(wires[1]) # <-- All the points which are appearing in both the wires
	# Now we return the smallest manhattam distance
	return min(abs(x) + abs(y) for x,y in inter)


def part2(data):
	wires = [generateMapping(wire) for wire in data]
	intersections = set(wires[0]).intersection(wires[1]) # <-- All the intersection points

	# Convert intersection points to steps in each wire
	wire1 = [wires[0].index(point)+1 for point in intersections]
	wire2 = [wires[1].index(point)+1 for point in intersections]
	
	# Return the minimum of the total steps taken by each wire to reach an intersection
	return min(wire1[i] + wire2[i] for i in range(len(intersections)))