#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import cos, sin, pi

split_data = True
completed = True 
raw_data = None # Not To be touched

def part1(data):
	px, py = 0, 0
	moveMap = {
		'N': (0, 1),
		'E': (1, 0),
		'S': (0, -1),
		'W': (-1, 0)
	}
	directions = [*moveMap.keys()]
	facing = 1
	for line in data:
		command, unit = line[:1], int(line[1:])
		if command in moveMap:
			dx, dy = moveMap[command]
			px += dx * unit
			py += dy * unit
		elif command == 'F':
			dx, dy = moveMap[directions[facing % 4]]
			px += dx * unit
			py += dy * unit
		elif command == 'R':
			facing += unit // 90
		elif command == 'L':
			facing -= unit // 90
	
	return abs(px) + abs(py)

def part2(data):
	px, py = 0, 0
	wx, wy = 10, 1
	moveMap = {
		'N': (0, 1),
		'E': (1, 0),
		'S': (0, -1),
		'W': (-1, 0)
	}

	for line in data:
		command, unit = line[:1], int(line[1:])
		if command in moveMap:
			dx, dy = moveMap[command]
			wx += dx * unit
			wy += dy * unit
		elif command == 'F':
			px += wx * unit
			py += wy * unit
		elif command == 'L':
			tx = cos(pi * unit / 180) * wx - sin(pi * unit / 180) * wy
			ty = sin(pi * unit / 180) * wx + cos(pi * unit / 180) * wy
			wx, wy = round(tx), round(ty)
		elif command == 'R':
			tx = cos(pi * unit / 180) * wx + sin(pi * unit / 180) * wy
			ty = -sin(pi * unit / 180) * wx + cos(pi * unit / 180) * wy
			wx, wy = round(tx), round(ty)
	
	return abs(px) + abs(py)
